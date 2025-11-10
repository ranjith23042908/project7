import json
class DepartmentResponse:
    id =None
    name = None
    remarks = None
    status = None

    def get(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
        # return json.dumps(self.to_dict())

    def set_id(self,id):
        self.id=id
    def set_name(self,name):
        self.name=name
    def set_remarks(self,remarks):
        self.remarks=remarks
    def set_status(self,status):
        self.status=status
