import json
class EmployeeResponse:
    id =None
    name = None
    age = None
    gender = None
    department_id = None
    salary = None
    status = None

    def get(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def set_id(self,id):
        self.id=id
    def set_name(self,name):
        self.name=name
    def set_age(self,age):
        self.age=age
    def set_gender(self,gender):
        self.gender=gender
    def set_department_id(self,department_id):
        self.department_id=department_id
    def set_salary(self,salary):
        self.salary=salary
    def set_status(self,status):
        self.status=status



