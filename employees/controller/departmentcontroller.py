import json
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from employees.service.departmentservice import Department_Service
from employees.models import Department
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from employees.data.request.departmentrequest import DepartmentRequest

@csrf_exempt
def create_department(request):
    if request.method == "POST":
        data = json.loads(request.body)
        data_obj=DepartmentRequest(data)
        service = Department_Service()
        dept = service.create_department_service(data_obj)
        return HttpResponse(json.dumps({"id": dept.id, "message": "Employee created"}),content_type="application/json")
    return HttpResponse(json.dumps({"error": "Invalid request method"}), content_type="application/json")

@csrf_exempt
def bulk_create_department(request):
    if request.method == "POST":
        data_list = json.loads(request.body)
        service = Department_Service()
        dept = service.bulk_create_department_service(data_list)
        return HttpResponse(json.dumps({"message":f"{len(dept)} Employee created"}),content_type="application/json")
    return HttpResponse(json.dumps({"error": "Invalid request method"}), content_type="application/json")

@csrf_exempt
def delete_department(request, dept_id):
    if request.method == "POST":
        service = Department_Service()
        result = service.delete_department_service(dept_id)
        return HttpResponse(json.dumps(result), content_type="application/json")
    return HttpResponse(json.dumps({"error": "Invalid request method"}), content_type="application/json")

@csrf_exempt
def update_department(request):
    if request.method == "GET":
        data = json.loads(request.body)
        service= Department_Service()
        result = service.update_department_service(data)
        return HttpResponse(json.dumps(result), content_type="application/json")
    return HttpResponse(json.dumps({"error": "Invalid request method"}), content_type="application/json")

@csrf_exempt
@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_all_department(request):
    if request.method == "GET":
        dept = Department.objects.all().values()
        return HttpResponse(json.dumps(list(dept)), content_type="application/json")
    return HttpResponse(json.dumps({"error": "Invalid request method"}), content_type="application/json")


@csrf_exempt
def department_table_download(request):
    if request.method  =="GET":
        service=Department_Service()
        Dept=service.department_table_download_Excel_service()
        return Dept
    return HttpResponse(json.dumps({"error": "Invalid request method"}), content_type="application/json")

@csrf_exempt
def get_show_department(request):
    try:
        if request.method == "GET":
            service=Department_Service()
            data=service.get_department_service()
            return HttpResponse(data.get(), content_type="application/json")
    except Exception as e:
        return HttpResponse(json.dumps({"error": "Not found"}), status=400, content_type="application/json")
    return HttpResponse(json.dumps({"error": "Invalid request method"}), content_type="application/json")

