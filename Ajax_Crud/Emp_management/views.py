import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from .models import Employee
from .forms import EmployeeForm
from django.views.decorators.csrf import csrf_exempt


#to view Employees
@csrf_exempt
def Employee_List(request):
    if request.method == 'GET' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        try:
            employees = list(Employee.objects.all().values())  # Get employee data as a list of dictionaries
            return JsonResponse(employees, safe=False)  # Return JSON data
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    # If it's not an AJAX request, render the full template
    employees = Employee.objects.all()
    return render(request, "Emp_list.html", {'employees': employees})
    

#create employees
@csrf_exempt
def createEmployee(request):
    if request.method == 'POST':
        try:
            # Extracting data directly from request.POST and request.FILES
            name = request.POST.get('name')
            email = request.POST.get('email')
            age = request.POST.get('age')
            gender = request.POST.get('gender')
            phone_no = request.POST.get('phoneNo')
            hno = request.POST.get('hno')
            street = request.POST.get('street')
            city = request.POST.get('city')
            state = request.POST.get('state')
            company_name = request.POST.get('companyName')
            from_date = request.POST.get('fromDate')
            to_date = request.POST.get('toDate')
            address = request.POST.get('address', 'Unknown address')
            qualification_name = request.POST.get('qualificationName')
            percentage = request.POST.get('percentage')
            title = request.POST.get('title')
            description = request.POST.get('description')
            photo = request.FILES.get('photo')

            # Create and save the Employee object
            employee = Employee(
                name=name,
                email=email,
                age=age,
                gender=gender,
                phoneNo=phone_no,
                hno=hno,
                street=street,
                city=city,
                state=state,
                companyName=company_name,
                fromDate=from_date,
                toDate=to_date,
                address=address,
                qualificationName=qualification_name,
                percentage=percentage,
                title=title,
                description=description,
                photo=photo  # This will handle file upload automatically
            )

            # Save the employee to the database
            employee.save()
            return JsonResponse({'message': 'Employee created successfully!'}, status=201)

        except KeyError as e:
            return JsonResponse({'error': f'Missing required field: {str(e)}'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

#delete employees
@csrf_exempt
def deleteEmployee(request, employee_id):
    if request.method == 'DELETE':
        try:
            employee = Employee.objects.get(id=employee_id)
            employee.delete()
            return JsonResponse({'message': 'Employee deleted successfully!'}, status=200)
        except Employee.DoesNotExist:
            return JsonResponse({'error': 'Employee not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

#edit and update employees





# @csrf_exempt
# def editEmployee(request, employee_id):
    try:
        employee = Employee.objects.get(id=employee_id)
    except Employee.DoesNotExist:
        return JsonResponse({'error': 'Employee not found'}, status=404)

    if request.method == 'GET':
        # Return employee data as JSON for pre-filling form
        employee_data = {
            'name': employee.name,
            'email': employee.email,
            'age': employee.age,
            'gender': employee.gender,
            'phoneNo': employee.phoneNo,
            'hno': employee.hno,
            'street': employee.street,
            'city': employee.city,
            'state': employee.state,
            'companyName': employee.companyName,
            'fromDate': employee.fromDate,
            'toDate': employee.toDate,
            'address': employee.address,
            'qualificationName': employee.qualificationName,
            'percentage': employee.percentage,
            'title': employee.title,
            'description': employee.description,
            'photo' :employee.photo,
            # Include any other fields you need to pre-populate
        }
        return JsonResponse(employee_data, status=200)

    if request.method == 'POST':
        try:
            # Update employee fields as already have it
            employee.name = request.POST.get('name', employee.name)
            employee.email = request.POST.get('email', employee.email)
            employee.age = request.POST.get('age', employee.age)
            employee.gender = request.POST.get('gender', employee.gender)
            employee.phoneNo = request.POST.get('phoneNo', employee.phoneNo)
            employee.hno = request.POST.get('hno', employee.hno)
            employee.street = request.POST.get('street', employee.street)
            employee.city = request.POST.get('city', employee.city)
            employee.state = request.POST.get('state', employee.state)
            employee.companyName = request.POST.get('companyName', employee.companyName)
            employee.fromDate = request.POST.get('fromDate', employee.fromDate)
            employee.toDate = request.POST.get('toDate', employee.toDate)
            employee.address = request.POST.get('address', employee.address)
            employee.qualificationName = request.POST.get('qualificationName', employee.qualificationName)
            employee.percentage = request.POST.get('percentage', employee.percentage)
            employee.title = request.POST.get('title', employee.title)
            employee.description = request.POST.get('description', employee.description)

            if 'photo' in request.FILES:
                employee.photo = request.FILES['photo']

            employee.save()
            return JsonResponse({'message': 'Employee updated successfully!'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)




@csrf_exempt  # Consider removing this for production
def editEmployee(request, employee_id):
    try:
        employee = Employee.objects.get(id=employee_id)
    except Employee.DoesNotExist:
        return JsonResponse({'error': 'Employee not found'}, status=404)

    if request.method == 'GET':
        # Return employee data as JSON for pre-filling form
        employee_data = {
            'name': employee.name,
            'email': employee.email,
            'age': employee.age,
            'gender': employee.gender,
            'phoneNo': employee.phoneNo,
            'hno': employee.hno,
            'street': employee.street,
            'city': employee.city,
            'state': employee.state,
            'companyName': employee.companyName,
            'fromDate': employee.fromDate,
            'toDate': employee.toDate,
            'address': employee.address,
            'qualificationName': employee.qualificationName,
            'percentage': employee.percentage,
            'title': employee.title,
            'description': employee.description,
            'photo': employee.photo.url if employee.photo else None,  # Ensure URL is returned
        }
        return JsonResponse(employee_data, status=200)

    if request.method == 'POST':
        try:
            # Update employee fields
            employee.name = request.POST.get('name', employee.name)
            employee.email = request.POST.get('email', employee.email)
            employee.age = request.POST.get('age', employee.age)
            employee.gender = request.POST.get('gender', employee.gender)
            employee.phoneNo = request.POST.get('phoneNo', employee.phoneNo)
            employee.hno = request.POST.get('hno', employee.hno)
            employee.street = request.POST.get('street', employee.street)
            employee.city = request.POST.get('city', employee.city)
            employee.state = request.POST.get('state', employee.state)
            employee.companyName = request.POST.get('companyName', employee.companyName)
            employee.fromDate = request.POST.get('fromDate', employee.fromDate)
            employee.toDate = request.POST.get('toDate', employee.toDate)
            employee.address = request.POST.get('address', employee.address)
            employee.qualificationName = request.POST.get('qualificationName', employee.qualificationName)
            employee.percentage = request.POST.get('percentage', employee.percentage)
            employee.title = request.POST.get('title', employee.title)
            employee.description = request.POST.get('description', employee.description)

            if 'photo' in request.FILES:
                employee.photo = request.FILES['photo']

            employee.save()
            return JsonResponse({'message': 'Employee updated successfully!'}, status=200)
        except Exception as e:
            print(f"Error updating employee: {str(e)}")  # Log the error
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)