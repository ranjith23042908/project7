import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
from employees.models import Employee
from employees.service.service import Service

@csrf_exempt
def addition(request):
    if request.method == "POST":
        data=json.loads(request.body)
        a=Service()
        x =int(data['a'])
        y =int(data['b'])
        z= a.addition_service(x, y)
        return HttpResponse(json.dumps(z), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"error":"Invalid request method"}), content_type="application/json")


@csrf_exempt
def subtraction(request):
    if request.method == "POST":
        data=json.loads(request.body)
        a=Service()
        x =int(data['a'])
        y =int(data['b'])
        z= a.subtraction_service(x, y)
        return HttpResponse(json.dumps(z), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"error":"Invalid request method"}), content_type="application/json")




#     -----------------------//------------------------


#
# import json
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from employees.service.service import AuthService
#
# @csrf_exempt
# def register_view(request):
#     if request.method == "POST":
#         try:
#             data = json.loads(request.body.decode("utf-8"))
#             username = data.get("username")
#             password = data.get("password")
#
#             service = AuthService()
#             result = service.register_service(username, password)
#
#             if "error" in result:
#                 return JsonResponse(result, status=400)
#
#             return JsonResponse(result, status=201)
#         except Exception as e:
#             return JsonResponse({"error": str(e)}, status=400)
#     return JsonResponse({"error": "Invalid request method"}, status=405)
#
#
# @csrf_exempt
# def login_view(request):
#     if request.method == "POST":
#         try:
#             data = json.loads(request.body.decode("utf-8"))
#             username = data.get("username")
#             password = data.get("password")
#
#             service = AuthService()
#             result = service.login_service(username, password)
#
#             if "error" in result:
#                 return JsonResponse(result, status=401)
#
#             return JsonResponse(result, status=200)
#         except Exception as e:
#             return JsonResponse({"error": str(e)}, status=400)
#     return JsonResponse({"error": "Invalid request method"}, status=405)
