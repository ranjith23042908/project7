import json
from employees.data.response.emailresponse import EmailResponse,SalaryResponse,AccountResponse
from employees.models import Email,Salary,Account

class Email_Service():

    def create_email_service(self, data):
        emp = Email.objects.create(
            name=data.get_name(),
            age=data.get_age(),
            email=data.get_email()
        )
        email_response=EmailResponse()
        email_response.set_id(emp.id)
        email_response.set_name(emp.name)
        email_response.set_age(emp.age)
        email_response.set_email(emp.email)

        return email_response


class Salary_Service():

    def create_salary_service(self, data):
        emp = Salary.objects.create(
            salary=data.get_salary(),
            email_id=data.get_email_id()
        )
        salary_response = SalaryResponse()
        salary_response.set_id(emp.id)
        salary_response.set_salary(emp.salary)
        salary_response.set_email_id(emp.email)
        return salary_response


import random
class Account_Service():
    def create_account_service(self, data):
        acc =Account.objects.create(
            name=data.get_name(),
            email=data.get_email(),
            pin=int(random.randint(1000,9999)),
            balance=data.get_balance(),
        )
        account_response=AccountResponse()
        account_response.set_id(acc.id)
        account_response.set_name(acc.name)
        account_response.set_email(acc.email)
        account_response.set_pin (acc.pin)
        account_response.set_balance(acc.balance)

        return account_response






