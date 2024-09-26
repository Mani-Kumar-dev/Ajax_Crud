
from django.urls import path
from .import views

urlpatterns = [
    path("",views.Employee_List,name="Employee_List"),
    path("create/",views.createEmployee,name="createEmployee"),
    path('delete_employee_url/<int:employee_id>/', views.deleteEmployee, name='delete_employee'),
    path('edit-employee/<int:employee_id>/', views.editEmployee, name='edit_employee'),
    
]