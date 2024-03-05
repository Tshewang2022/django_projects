from django.shortcuts import redirect, render
from django.http import HttpResponse
import json
import os
from django.conf import settings
from  .myForm  import MyForm
from .models import User
from  .myModelForm import UserForm

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. This is the index page.")

def home(request):
    return HttpResponse("Hello, world. This is the home page.")
    
def mydata(request,param):
    context={ 'param': param }
    return render(request,'myprofile.html',context)

def usersdata(request):
    filePath= os.path.join(settings.STATIC_ROOT,'users.json')
    with open(filePath) as f:
        userData=json.load(f)
    for user in userData:
        user['name']=user['name'].capitalize()
        user['gender']=user['gender'].upper()
        
    context={'users':userData}
    return render(request ,'users.html',context)
    
def contactForm(request):
    if request.method=='POST':
        myName=request.POST.get('myName')
        myEmail=request.POST.get('myEmail')
        myQuery=request.POST.get('myQuery')
        # return redirect('success', myName=myName, myEmail=myEmail,myQuery=myQuery)
       
    
        return render(request, 'successPage.html',{'myName':myName, 'myEmail':myEmail, 'myQuery':myQuery})
        
    return render(request, 'contactForm.html')
def successPage(request):
    myName = request.GET.get('myName')
    return HttpResponse(myName)
    # myName=request.GET.get('myName')
    # myEmail=request.GET.get('myEmail')
    # myQuery=request.GET.get('myQuery')
    # return render(request, 'successPage.html',{'myName':myName, 'myEmail':myEmail, 'myQuery':myQuery})

def myForm(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            # Access cleaned form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            # Process the data as needed
            return render(request, 'success.html', {'name': name, 'email': email, 'password':password})
    else:
        form = MyForm()
    return render(request, 'my_form.html', {'form': form})
def next_page(request):
    return render(request,'success.html')
def myProfile(request):
	users = User.objects.all()
	return render(request, 'myprofileDet.html', {'users': users})

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return render(request, 'create_user.html')
        
            # return redirect('myprofile')  # Redirect to the profile page after successful submission
    else:
        form = UserForm()
    return render(request, 'create_user.html', {'form': form})


