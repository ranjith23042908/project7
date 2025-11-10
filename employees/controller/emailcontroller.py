import json
from employees.models import Email,Salary,Account
from django.core import mail
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from employees.data.request.emailrequest import EmailRequest,SalaryRequest,AccountRequest
from employees.service.emailservice import Email_Service,Salary_Service,Account_Service
from project7 import settings
import random




@csrf_exempt
@api_view(['POST'])
def create_email(request):
    try:
        if request.method == "POST":
            data = json.loads(request.body)
            data_obj=EmailRequest(data)
            service = Email_Service()
            emp = service.create_email_service(data_obj)
            return HttpResponse(json.dumps({"id": emp.id, "message": "Mail created"}),content_type="application/json")
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)
    return HttpResponse(json.dumps({"error": "Invalid request method"}), content_type="application/json")

@csrf_exempt
@api_view(['POST'])
def create_salary(request):
    if request.method == "POST":
        data = json.loads(request.body)
        data_obj=SalaryRequest(data)
        service = Salary_Service()
        emp = service.create_salary_service(data_obj)
        return HttpResponse(json.dumps({"id": emp.id, "message": "salary created"}),content_type="application/json")
    return HttpResponse(json.dumps({"error": "Invalid request method"}), content_type="application/json")


@csrf_exempt
def email_send(request):
    if request.method == "POST":
        try:
            e=request.GET.get("EMID")
            # email_to=int(e)
            cc=json.loads(request.body)
            cc_values =list(cc.values())

            if not e:
                return JsonResponse({"error": "EMID is required"}, status=400)

            try:
                emil_obj=Email.objects.get(id=e)
                salary_details=Salary.objects.get(email_id=e)

            except Email.DoesNotExist:
                return JsonResponse({"error": f"Employee not found for id {e}"}, status=404)
            except Salary.DoesNotExist:
                return JsonResponse({"error": f"EmployeeDetails not found for id {e}"}, status=404)

            message=f"""\nHello {emil_obj.name},\nYour salary of ₹{salary_details.salary} has been credited successfully.\nRegards,\nHR Department"""


            email = EmailMessage(
                subject="Salary Credited Notification",
                body=message.upper(),
                from_email=settings.EMAIL_HOST_USER,
                to=[emil_obj.email],
                cc=cc_values,
            )
            email.send(fail_silently=False)
            return JsonResponse({"message": f"salary credited successfully to {emil_obj.name}"}, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "Method not supported"}, status=405)

@csrf_exempt
def send_single_email(request):
    if request.method == "POST":
        try:
            cc=json.loads(request.body)
            cc_values =list(cc.values())

            send_mail(
    subject="Test Mail",
    message="This is a test email from Django!",
    from_email=settings.EMAIL_HOST_USER,
    recipient_list=cc_values,
    fail_silently=False
)
            return JsonResponse({"message": f"salary credited successfully"})

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "Method not supported"}, status=405)


@csrf_exempt
@api_view(['POST'])
def create_account(request):
    try:
        if request.method == "POST":
            data = json.loads(request.body)
            data_obj=AccountRequest(data)
            service = Account_Service()
            acc = service.create_account_service(data_obj)
            return HttpResponse(json.dumps({"id": acc.id, "message": "Account created"}),content_type="application/json")
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)
    return HttpResponse(json.dumps({"error": "Invalid request method"}), content_type="application/json")

@csrf_exempt
def send_pin_email(request):
    if request.method == "POST":
        try:
            e = request.GET.get("PIN")
            if not e:
                return JsonResponse({"error": "PIN is required"}, status=400)

            cc = json.loads(request.body)
            cc_values = list(cc.values())

            try:
                account = Account.objects.get(id=e)

            except Email.DoesNotExist:
                return JsonResponse({"error": f"Employee not found for id {e}"}, status=404)


            send_mail(
    subject = "Your ATM PIN",
    message = f"Hello {account.name},\n\nYour new ATM PIN is: {account.pin}\nKeep it secure!",
    from_email = settings.EMAIL_HOST_USER,
    recipient_list = cc_values,
    fail_silently = False
)
            return JsonResponse({"message": f"ATM PIN successfully to {account.pin}"})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "Method not supported"}, status=405)

