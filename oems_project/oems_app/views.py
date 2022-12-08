from datetime import datetime

from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, HttpResponse
from .models import Employee, Role, Department

# Create your views here.


def index(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'oems_app/index.html', context)


def all_emp(request):
    emps = Employee.objects.all()

    context = {
        'emps': emps,
    }
    return render(request, 'oems_app/all_emp.html', context)


def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dept = int(request.POST['dept'])
        role = int(request.POST['role'])
        salary = int(request.POST['salary'])
        phone = request.POST['phone']

        new_emp = Employee(first_name=first_name,
                           last_name=last_name,
                           dept_id=dept,
                           role_id=role,
                           salary=salary,
                           hire_date=datetime.now(),
                           phone=phone
                           )
        new_emp.save()
        return HttpResponseRedirect(reverse('index'))
    elif request.method == 'GET':
        return render(request, 'oems_app/add_emp.html')
    else:
        return HttpResponse("Une erreur est survenue. L'employé n'a pas pû être ajouté.")


def remove_emp(request):
    emps = Employee.objects.all()
    trash_logo = '../../static/oems_app/images/trash.png'
    context = {
        'emps': emps,
        'trash_logo': trash_logo
    }
    return render(request, 'oems_app/remove_emp.html', context)


def delete_emp(request, emp_id=0):
    if emp_id:
        try:
            emp_to_delete = Employee.objects.get(id=emp_id)
            emp_to_delete.delete()
            return HttpResponseRedirect(reverse('index'))
        except:
            return HttpResponse("Un problème a été rencontré lors de l'opération. La suppression a échoué.")


def filter_emp(request):
    if request.method == 'POST':
        try:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            dept = request.POST['dept']
            role = request.POST['role']

            emps = Employee.objects.all()

            if first_name:
                filtered_emps = emps.filter(Q(first_name__icontains=first_name))
            if last_name:
                filtered_emps = emps.filter(Q(last_name__icontains=last_name))
            if dept:
                filtered_emps = emps.filter(dept__name=dept)
            if role:
                filtered_emps = emps.filter(role__name=role)

            context = {
                'emps': filtered_emps,
            }
            return render(request, 'oems_app/all_emp.html', context)
        except:
            return render(request, 'oems_app/filter_emp.html')
    elif request.method == 'GET':
        return render(request, 'oems_app/filter_emp.html')
    else:
        return HttpResponse('Une erreur est survenue')


def update_emp(request):
    emps = Employee.objects.all()
    edit_logo = '../../static/oems_app/images/edit.png'
    context = {
        'emps': emps,
        'edit_logo': edit_logo
    }
    return render(request, 'oems_app/update_emp.html', context)


# à créer avec un formulaire comme pour l'ajout mais cette fois-ci pour modifier une ou plusieurs données
def modify_emp(request, emp_id=0):
    pass
    return
