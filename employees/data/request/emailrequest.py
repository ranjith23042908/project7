class EmailRequest:
    name =None
    age = None
    email=None

    def __init__(self, data):
        if "name" in data:
            self.name = data["name"]
        if "age" in data:
            self.age = data["age"]
        if "email" in data:
            self.email = data["email"]

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_email(self):
        return self.email

class SalaryRequest:
    salary=None
    email_id=None

    def __init__(self, data):
        if "salary" in data:
            self.salary = data["salary"]
        if "email_id" in data:
            self.email_id = data["email_id"]

    def get_salary(self):
        return self.salary

    def get_email_id(self):
        return self.email_id


class AccountRequest:
    name =None
    email=None
    pin=None
    balance=None

    def __init__(self, data):
        if "name" in data:
            self.name = data["name"]
        if "email" in data:
            self.email = data["email"]
        if "pin" in data:
            self.pin = data["pin"]
        if "balance" in data:
            self.balance = data["balance"]


    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_pin(self):
        return self.pin

    def get_balance(self):
        return self.balance