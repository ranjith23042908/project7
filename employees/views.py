from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def home(request):
    if request.method =="GET":
        return HttpResponse("Hello, Django Middleware!")
    return HttpResponse("Invalid request method")


from django.http import JsonResponse

@csrf_exempt
def api_test(request):
    if request.method =="GET":
        return JsonResponse({"message": "Hello, Django Middleware!"})
    return HttpResponse("Invalid request method")



