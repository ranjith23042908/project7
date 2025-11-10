import json,io
from http.client import responses
from itertools import count

from django.views.decorators.http import condition

from employees.data.pagination.employeepaginator import EmployeePaginator
from employees.data.response.employeeresponse import EmployeeResponse
from employees.models import Employee ,Department
from django.db.models import Avg, Sum, Count, Q
from django.http import HttpResponse, JsonResponse, FileResponse, StreamingHttpResponse
import pandas as pd
from employees.util.employeeutil import EmployeeGender, get_employeegender,get_employeestatus
from employees.data.pagination.defaultlist import DefaultList


class Employee_Service():

    def create_employee_service(self, data):
        emp = Employee.objects.create(
            name=data.get_name(),
            age=data.get_age(),
            gender=data.get_gender(),
            department_id=data.get_department_id(),
            salary=data.get_salary(),
            status=data.get_status(),
        )
        employee_response=EmployeeResponse()
        employee_response.set_id(emp.id)
        employee_response.set_name(emp.name)
        employee_response.set_age(emp.age)
        employee_response.set_gender(emp.gender)
        employee_response.set_department_id(emp.department)
        employee_response.set_salary(emp.salary)
        employee_response.set_status(emp.status)
        return employee_response

    def bulk_create_employee_service(self,data_list):
        employee = []
        for emp in data_list:
            employee.append(Employee(
                name=emp.get_name(),
                age=emp.get_age(),
                gender=emp.get_gender(),
                department_id=emp.get_department_id(),
                salary=emp.get_salary(),
                status=emp.get_status(),
            ))
        Employee.objects.bulk_create(employee)
        response_data = []
        for emp in employee:
            employee_response = EmployeeResponse()
            employee_response.set_id(emp.id)
            employee_response.set_name(emp.name)
            employee_response.set_age(emp.age)
            employee_response.set_gender(emp.gender)
            employee_response.set_department_id(emp.department)
            employee_response.set_salary(emp.salary)
            employee_response.set_status(emp.status)
            response_data.append(employee_response)
        return response_data

    def delete_employee_service(self, data):
        try:
            emp = Employee.objects.get(id=data["id"])
            emp.delete()
            return (json.dumps({"status": "success", "message": f"Employee {data["id"]} deleted"}))

        except Employee.DoesNotExist:
            return (json.dumps({"status": "error", "message": "Employee not found"}))

    def bulk_delete_employee_service(self, data):
        try:
            employee=[]
            for emp_id in data:
                employee.append(emp_id["id"])
            emp = Employee.objects.filter(id__in=employee).delete()
            return (json.dumps({"status": "success", "message": "Employee deleted"}))

        except Employee.DoesNotExist:
            return (json.dumps({"status": "error", "message": "Employee not found"}))


    def update_employee_service(self,data):
        try:
            emp = Employee.objects.get(id=data["id"])
            emp.name = data.get("name", emp.name)
            emp.age = data.get("age", emp.age)
            emp.gender = data.get("gender", emp.gender)
            emp.department = data.get("department", emp.department)
            emp.salary = data.get("salary", emp.salary)
            emp.status = data.get("status", emp.status)
            emp.save()
            return {"status": "success", "message": f"Employee {emp.id} updated"}
        except Employee.DoesNotExist:
            return {"status": "error", "message": "Employee not found"}
        except Exception as e:
            return  JsonResponse({"error": str(e)},status=400)

    def bulk_update_employee_service(self,data_obj):
        try:
            employee=[]
            for data in data_obj:
                emp = Employee.objects.get(id=data["id"])
                emp.name = data.get("name", emp.name)
                emp.age = data.get("age", emp.age)
                emp.gender = data.get("gender", emp.gender)
                emp.department_id = data.get("department_id", emp.department_id)
                emp.salary = data.get("salary", emp.salary)
                emp.status = data.get("status", emp.status)
                employee.append(emp)
            Employee.objects.bulk_update(employee,["name", "age", "gender", "department", "salary", "status"])
            return {"status": "success", "message": f"Employee {emp.id} updated"}
        except Employee.DoesNotExist:
            return {"status": "error", "message": "Employee not found"}

    def get_employee_service(self):
        try:
            condition= Q(status=1)  | Q(status=2) | Q(status=0)
            empp=Employee.objects.filter(condition)
            employee_append=DefaultList()
            for emp in empp:
                employee_response = EmployeeResponse()
                employee_response.set_id(emp.id)
                employee_response.set_name(emp.name)
                employee_response.set_age(emp.age)

                employee_response.set_gender(get_employeegender(emp.gender).text)

                employee_response.set_department_id(emp.department_id)
                employee_response.set_salary(emp.salary)
                employee_response.set_status(get_employeestatus(emp.status).text)

                employee_append.append(employee_response)
            return employee_append
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    def get_single_id_employee_service(self,emp_id):
        employee=Employee.objects.get(id=emp_id)
        emp ={
            "id":employee.id,
            "name":employee.name,
            "age":employee.age,
            "gender": employee.gender,
            "department_id": employee.department_id,
            "salary": employee.salary,
            "status": employee.status,
        }
        return emp


    def get_limited_employees_service(self, limit):
        employees = Employee.objects.all()[:limit]
        return [{"id": e.id, "name": e.name} for e in employees]

    def salary_aggregates_service(self):
        return Employee.objects.aggregate(
            avg_salary=Avg("salary"),
            total_salary=Sum("salary"),
            emp_count=Count("id")
        )

    def count_department_service(self):
        depts = Department.objects.annotate(emp_count=Count("employee"))
        return [{"id": d.id, "name": d.name, "employees": d.emp_count} for d in depts]


    def employee_table_download_excel_service(self):
        emp= Employee.objects.all().values()
        depm=Department.objects.all().values()
        df1=pd.DataFrame(list(emp))
        df2=pd.DataFrame(list(depm))
        df=df1.merge(df2, how='right',left_on="department_id",right_on='id')

        output = io.BytesIO()
        writer = pd.ExcelWriter(output, engine="xlsxwriter")
        df.to_excel(writer, sheet_name="Sheet1", index=False)
        writer.close()

        output.seek(0)

        response = StreamingHttpResponse(output,content_type="application/octet-stream")
        response["Content-Disposition"] = 'attachment; filename="employee.xlsx"'
        return response

    def employee_pagination_service(self,request,data,output_page):
        all_employee=Employee.objects.filter(status=data["status"])
        count=len(all_employee)
        empp=Employee.objects.filter(status=data["status"])[output_page.get_offset():output_page.get_limit()]
        employee_append=DefaultList()

        for emp in empp:
            employee_response = EmployeeResponse()

            employee_response.set_id(emp.id)
            employee_response.set_name(emp.name)
            employee_response.set_age(emp.age)
            employee_response.set_gender(emp.gender)
            employee_response.set_department_id(emp.department_id)
            employee_response.set_salary(emp.salary)
            employee_response.set_status(emp.status)

            employee_append.append(employee_response)

        lst=EmployeePaginator(all_employee,output_page.get_index(),10)
        lst.count=count
        employee_append.set_pagination(lst)
        return employee_append


