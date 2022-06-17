from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render

from .models import Student



# Create your views here.
def add_data(request):
    if request.method =='POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        user = Student(name=name, email=email, password=password)
        user.save()
        return redirect('add_data')

    usr= Student.objects.all()
    return render(request, 'add_data_and_show.html',{'user':usr})

def delete_data(request,id):
    ur=Student.objects.get(pk=id)
    ur.delete()
    return redirect('add_data')

def edit_data(request,id):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        user = Student(pk=id, name=name, email=email, password=password)
        user.save()
        return redirect('add_data')
    else:
        stud = Student.objects.filter(pk=id)
        context ={
            'user':stud
        }

    return render(request, 'update_data.html',context)
        
        
        
   