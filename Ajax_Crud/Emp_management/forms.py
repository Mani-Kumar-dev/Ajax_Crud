from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            'name', 'email', 'age', 'gender', 'phoneNo', 'hno', 
            'street', 'city', 'state', 'companyName', 'fromDate', 
            'toDate', 'address', 'qualificationName', 'percentage', 
            'title', 'description', 'photo'
        ]
        widgets = {
            'gender': forms.RadioSelect(choices=Employee.GENDER_CHOICES),
            'fromDate': forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'}),
            'toDate': forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'}),
        }
