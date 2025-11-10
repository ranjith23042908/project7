import io
from os import write

import pandas as pd
from django.db.models import Q
from django.http import StreamingHttpResponse, JsonResponse

from employees.data.pagination.defaultlist import DefaultList
from employees.data.response.departmentresponse import DepartmentResponse
from employees.models import Department
import json


class Department_Service():

    def create_department_service(self, data):
        dept = Department.objects.create(
            name=data.get_name(),
            remarks=data.get_remarks(),
            status=data.get_status()
        )
        # dept = Department.objects.create(
        #     name=data["name"],
        #     remarks=data["remarks"],
        #     status=data["status"]
        # )
        return dept

    def bulk_create_department_service(self,data_list):
        department = []
        for dept in data_list:
            department.append(Department(
                name=dept["name"],
                remarks=dept["remarks"],
                status=dept["status"]
            ))
        Department.objects.bulk_create(department)
        return department

    def delete_department_service(self, dept_id):
        try:
            dept = Department.objects.get(id=dept_id)
            dept.delete()
            return (json.dumps({"status": "success", "message": f"Department {dept_id} deleted"}))

        except Department.DoesNotExist:
            return (json.dumps({"status": "error", "message": "Department not found"}))

    def update_department_service(self,data):
        try:
            dept = Department.objects.get(id=data["id"])
            dept.name = data.get("name", dept.name)
            dept.remarks = data.get("remarks", dept.remarks)
            dept.status = data.get("status", dept.status)
            dept.save()
            return {"status": "success", "message": f"Department {dept.id} updated"}
        except Department.DoesNotExist:
            return {"status": "error", "message": "Department not found"}

    def department_table_download_Excel_service(self):
        Dept=Department.objects.all().values()
        df=pd.DataFrame(list(Dept))

        output=io.BytesIO()

        writer=pd.ExcelWriter(output, engine="xlsxwriter")
        df.to_excel(writer, sheet_name="sheet1" ,index= False)
        writer.close()

        output.seek(0)

        response = StreamingHttpResponse(output, content_type="application/octet-stream")
        response["Content-Disposition"] = 'attachment; filename="department.xlsx"'
        return response

    def get_department_service(self):
        try:
            department=Department.objects.all()
            department_append=DefaultList()
            for dept in department:
                department_response = DepartmentResponse()
                department_response.set_id(dept.id)
                department_response.set_name(dept.name)
                department_response.set_remarks(dept.remarks)
                department_response.set_status(dept.status)
                department_append.append(department_response)
            return department_append
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)