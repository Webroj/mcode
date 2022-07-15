from django.shortcuts import render, HttpResponseRedirect
from myapp.forms import StudentRegistration
from .models import User

# Create your views here.

# this function will add new item and show all item
def add_show(request):
    if request.method=="POST":
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            un=fm.cleaned_data['name']
            ue=fm.cleaned_data['email']
            up=fm.cleaned_data['password']
            reg=User(name=un, email=ue, password=up)
            reg.save()
            fm=StudentRegistration()
        # print("POST request Ayi h")
    else:
        fm=StudentRegistration()
    stud=User.objects.all()
        # print('Get Request Aayi hai ')
    return render(request, 'add-show.html', {'abc':fm, 'stu':stud})

# this function will update and edit

def update_data(request, id):
    if request.method=="POST":
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(instance=pi)    
    return render(request, 'update.html', {'form':fm})

# This function will delete data
 
def delete_data(request, id):
    if request.method=="POST":
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

    

