class DepartmentRequest:
    name=None
    remarks=None
    status=None
    def __init__(self,data):
        if "name" in data:
            self.name=data["name"]
        if "remarks" in data:
            self.remarks=data["remarks"]
        if "status" in data:
            self.status=data["status"]

    def get_name(self):
        return self.name
    def get_remarks(self):
        return self.remarks
    def get_status(self):
        return self.status