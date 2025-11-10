from employees.data.pagination.emplitelist import EmpLiteList
from employees.data.pagination.defaultlist import DefaultList

class EmployeeGender:
    MALE = "1"
    FEMALE = "2"
    OTHER = "3"

    MALE_TEXT = "MALE"
    FEMALE_TEXT = "FEMALE"
    OTHER_TEXT="OTHER"

def get_employeegender(number):
    emplite = DefaultList()
    if number == EmployeeGender.MALE:
        emplite.id=EmployeeGender.MALE
        emplite.text=EmployeeGender.MALE_TEXT
        return emplite
    elif number == EmployeeGender.FEMALE:
        emplite.id=EmployeeGender.FEMALE
        emplite.text=EmployeeGender.FEMALE_TEXT
        return emplite
    elif number == EmployeeGender.OTHER:
        emplite.id=EmployeeGender.OTHER
        emplite.text=EmployeeGender.OTHER_TEXT
        return emplite
    else:
        emplite.id = None
        emplite.text = "UNKNOWN"
    return emplite


class EmployeeStatus:
    ZERO=0
    ONE= 1
    TWO=2

    ZERO_VAL="ZERO"
    ONE_VAL="ONE"
    TWO_VAL="TWO"

def get_employeestatus(number):
    emplite=DefaultList()
    if (number == EmployeeStatus.ONE):
        emplite.id=EmployeeStatus.ONE
        emplite.text=EmployeeStatus.ONE_VAL
        return emplite
    elif (number == EmployeeStatus.TWO):
        emplite.id=EmployeeStatus.TWO
        emplite.text=EmployeeStatus.TWO_VAL
        return emplite
    elif (number == EmployeeStatus.ZERO):
        emplite.id=EmployeeStatus.ZERO
        emplite.text=EmployeeStatus.ZERO_VAL
        return emplite
    else:
        emplite.id=None
        emplite.text="UNKNOWN"
    return emplite


















