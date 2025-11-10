class EmployeeRequest:
    name =None
    age = None
    gender = None
    department_id = None
    salary = None
    status = None

    def __init__(self, data):
        if "name" in data:
            self.name = data["name"]
        if "age" in data:
            self.age = data["age"]
        if "gender" in data:
            self.gender = data["gender"]
        if "department" in data:
            self.department = data["department"]
        if "salary" in data:
            self.salary = data["salary"]
        if "status" in data:
            self.status = data["status"]

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_gender(self):
        return self.gender

    def get_department_id(self):
        return self.department_id

    def get_salary(self):
        return self.salary

    def get_status(self):
        return self.status

