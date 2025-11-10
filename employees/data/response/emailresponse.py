import json
class EmailResponse:
    id =None
    name = None
    age = None
    email=None

    def get(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def set_id(self,id):
        self.id=id
    def set_name(self,name):
        self.name=name
    def set_age(self,age):
        self.age=age
    def set_email(self,email):
        self.email=email

class SalaryResponse:
    id =None
    salary=None
    email_id=None

    def get(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def set_id(self,id):
        self.id=id
    def set_salary(self,salary):
        self.salary=salary
    def set_email_id(self,email_id):
        self.email_id=email_id

import json
class AccountResponse:
    id =None
    name = None
    email = None
    pin=None
    balance=None

    def get(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def set_id(self,id):
        self.id=id
    def set_name(self,name):
        self.name=name
    def set_email(self,email):
        self.email=email
    def set_pin(self,pin):
        self.pin=pin
    def set_balance(self,balance):
        self.balance=balance

