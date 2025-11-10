import json

import pandas as pd
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from employees.data.pagination.employeepage import EmployeePage
from employees.data.response.employeeresponse import EmployeeResponse
from employees.data.request.employeerequest import EmployeeRequest
from employees.service.employeeservice import Employee_Service
from employees.models import Employee, Department
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


@csrf_exempt
@api_view(['POST'])
def create_employee(request):
    if request.method == "POST":
        data = json.loads(request.body)
        data_obj=EmployeeRequest(data)
        service = Employee_Service()
        emp = service.create_employee_service(data_obj)
        return HttpResponse(json.dumps({"id": emp.id, "message": "Employee created"}),content_type="application/json")
    return HttpResponse(json.dumps({"error": "Invalid request method"}), content_type="application/json")

@csrf_exempt
def bulk_create_employee(request):
    if request.method == "POST":
        data_list = json.loads(request.body)
        data_obj = [EmployeeRequest(emp_data) for emp_data in data_list]
        service = Employee_Service()
        service_data = service.bulk_create_employee_service(data_obj)
        return HttpResponse(json.dumps({"message":f"{len(service_data)} Employee created"}),content_type="application/json")
    return HttpResponse(json.dumps({"error": "Invalid request method"}), content_type="application/json")

@csrf_exempt
def delete_employee(request):
    if request.method == "POST":
        data = json.loads(request.body)
        service = Employee_Service()
        result = service.delete_employee_service(data)
        return HttpResponse(result)
    return HttpResponse(json.dumps({"error": "Invalid request method"}), content_type="application/json")

@csrf_exempt
def bulk_delete_employee(request):
    if request.method == "POST":
        data = json.loads(request.body)
        service = Employee_Service()
        result = service.bulk_delete_employee_service(data)
        return HttpResponse(result)
    return HttpResponse(json.dumps({"error": "Invalid request method"}), content_type="application/json")
@csrf_exempt
def update_employee(request):
    if request.method == "POST":
        data = json.loads(request.body)
        service= Employee_Service()
        result = service.update_employee_service(data)
        return HttpResponse(json.dumps(result), content_type="application/json")
    return HttpResponse(json.dumps({"error": "Invalid request method"}), content_type="application/json")

@csrf_exempt
def bulk_update_employee(request):
    if request.method == "POST":
        data = json.loads(request.body)
        service= Employee_Service()
        result = service.bulk_update_employee_service(data)
        return HttpResponse(json.dumps(result), content_type="application/json")
    return HttpResponse(json.dumps({"error": "Invalid request method"}), content_type="application/json")

@csrf_exempt
@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_all_employee(request):
    try:
        if request.method == "POST":
            service=Employee_Service()
            data=service.get_employee_service()
            return HttpResponse(data.get(), content_type="application/json")
    except Exception as e:
        return Response(json.dumps({"error": "Not found"}), status=404, content_type="application/json")
    return HttpResponse(json.dumps({"error": "Invalid request method"}), content_type="application/json")




def get_single_id_employee(request,emp_id):
    try:
        if request.method == "GET":
            service=Employee_Service()
            emp=service.get_single_id_employee_service(emp_id)
            return HttpResponse(json.dumps(emp), content_type="application/json")
    except Employee.DoesNotExist:
            return HttpResponse(json.dumps({"error": "Not found"}), status=404,content_type="application/json")
    return HttpResponse(json.dumps({"error": "Invalid request method"}), content_type="application/json")


def get_limited_employees(request, limit):
    if request.method == "GET":
        service= Employee_Service()
        data = service.get_limited_employees_service(limit)
        return HttpResponse(json.dumps(data), content_type="application/json")
    return HttpResponse(json.dumps({"error": "Invalid request method"}), content_type="application/json")


def  salary_aggregates_employees(request):
    if request.method == "GET":
        service=Employee_Service()
        data = service.salary_aggregates_service()
        return HttpResponse(json.dumps(data), content_type="application/json")
    return HttpResponse(json.dumps({"error": "Invalid request method"}), content_type="application/json")

def get_department_counts(request):
    if request.method == "GET":
        service= Employee_Service()
        data = service.count_department_service()
        return HttpResponse(json.dumps(data), content_type="application/json")
    return HttpResponse(json.dumps({"error": "Invalid request method"}), content_type="application/json")


def download_employees_excel(request):
    if request.method == "GET":
        service=Employee_Service()
        emp=( service.employee_table_download_excel_service())
        return emp
    return HttpResponse(json.dumps({"error": "Invalid request method"}), content_type="application/json")

@csrf_exempt
def employee_pagination(request):
    try:
        if request.method == "POST":
            data=json.loads(request.body)
            page=request.GET.get("page",1)
            page=int(page)
            output_page=EmployeePage(page,10)

            service=Employee_Service()
            emp=service.employee_pagination_service(request,data,output_page)
            return HttpResponse(emp.get(), content_type="application/json")
    except Exception as e:
        return JsonResponse({"error": str(e)},status=400)

    return HttpResponse(json.dumps({"error": "Invalid request method"}), content_type="application/json")

@csrf_exempt
def view(request):
    data=Employee.objects.all().values()
    data_list=list(data)
    return HttpResponse(json.dumps(data_list),content_type="application/json")

# --------------//---------------

@csrf_exempt
def upload_department_excel(request):
    if request.method == 'POST':
        try:
            excel_file = request.FILES.get('file')
            if not excel_file:
                return JsonResponse({'status': 'error', 'message': 'No file uploaded'}, status=400)

            # Read Excel
            df = pd.read_excel(excel_file)

            # Normalize headers
            df.columns = df.columns.str.strip().str.lower()

            # Required columns
            required_cols = ['name', 'remarks', 'status']
            if not all(col in df.columns for col in required_cols):
                return JsonResponse({'status': 'error', 'message': f'Missing columns. Required: {required_cols}'}, status=400)

            created = 0
            errors = []

            for _, row in df.iterrows():
                try:
                    Department.objects.update_or_create(
                        name=row['name'],
                        defaults={
                            'remarks': row['remarks'],
                            'status': int(row['status'])
                        }
                    )
                    created += 1
                except Exception as e:
                    errors.append(str(e))

            return JsonResponse({
                'status': 'success',
                'inserted_records': created,
                'errors': errors
            })

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

    return JsonResponse({'status': 'error', 'message': 'Only POST method allowed'}, status=405)



























