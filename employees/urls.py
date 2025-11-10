"""
URL configuration for project7 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from employees import views
from employees.controller import controller,departmentcontroller,employeecontroller,emailcontroller
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('addition', controller.addition),
    path('subtraction', controller.subtraction),
    # Employee CRUD
    path('create_employee', employeecontroller.create_employee),
    path('bulk_create_employee', employeecontroller.bulk_create_employee),
    path('delete_employee',employeecontroller.delete_employee),
    path('update_employee',employeecontroller.update_employee),
    path('get_employee',employeecontroller.get_all_employee),
    path('get_employee/<int:emp_id>',employeecontroller.get_single_id_employee),
    path('employee_pagination',employeecontroller.employee_pagination),
    path('bulk_update_employee',employeecontroller.bulk_update_employee),
    path('bulk_delete_employee',employeecontroller.bulk_delete_employee),
    path('view',employeecontroller.view),

    # Department CRUD
    path('create_department',departmentcontroller.create_department),
    path('bulk_create_department', departmentcontroller.bulk_create_department),
    path('delete_department/<int:dept_id>',departmentcontroller.delete_department),
    path('update_department',departmentcontroller.update_department),
    path('get_department',departmentcontroller.get_all_department),
    path('get_show_department',departmentcontroller.get_show_department),

    path('upload_department_excel', employeecontroller.upload_department_excel),

    path("employees_limited/<int:limit>", employeecontroller.get_limited_employees),
    path("employees_aggregate", employeecontroller.salary_aggregates_employees),
    path("department_count", employeecontroller.get_department_counts),

    path('get_auth_token',obtain_auth_token),
    path('employee_download_excel',employeecontroller.download_employees_excel),
    path('department_download_excel',departmentcontroller.department_table_download),

    # Email
    path('create_email',emailcontroller.create_email),
    path('create_salary',emailcontroller.create_salary),
    path('create_account',emailcontroller.create_account),
    path('email_send',emailcontroller.email_send),
    path('send_single_email',emailcontroller.send_single_email),
    path('send_pin_email',emailcontroller.send_pin_email),


    # path('test',views.home),
    # path('api_test',views.api_test),
    # path('register_view',controller.register_view),
    # path('login_view',controller.login_view),
]
