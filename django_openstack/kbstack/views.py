from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response



from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
from django.views.generic import *
from .forms import UserForm
from openstack import connection
from . import service
from service import *

def index(request):
    return render(request, 'kbstack/index.html')

####################################################################################
def image_list(request):
    image = list_images()
    return render(request, 'kbstack/image_list.html', {'image': image})

####################################################################################
def flavor_list(request):
    flavor = list_flavors()
    return render(request, 'kbstack/flavor_list.html', {'flavor': flavor})



####################################################################################



def instance_list(request):
    server = list_servers()
    image = list_images()
    network = list_networks()
    return render(request, 'kbstack/instance_list.html', {'server': server})


####################################################################################

def create_instance(request):
    if request.method == 'POST':
        print("Create Server:")
        instance_name = request.POST['instance']
        image_name = request.POST['image']
        flavor_name = request.POST['flavor']
        create_server(instance_name,image_name,flavor_name)
    return render(request, 'kbstack/index.html')

#####################################################################################

def get_create_instance_form(request):
    image = list_images()
    flavor = list_flavors()
    return render(request, 'kbstack/create_instance.html', {'image':image, 'flavor':flavor})

#####################################################################################

def get_delete_instance_form(request):
    server = list_servers()
    return render(request, 'kbstack/delete_instance.html', {'server':server})

####################################################################################

def delete_instance(request):
    if request.method == 'POST':
        print("Deleted Server:")
        instance_name = request.POST['instance']
        delete_server(instance_name)
    return render(request, 'kbstack/index.html')


# class UserFormView(View):
#     from_class = UserForm
#     template_name = 'kbstack/login.html'
#
#     def get(self,request):
#         form = self.from_class(None)
#         return render(request,self.template_name,{'form':form})
#
#     def login(self,request):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user.set_password(password)
#             user.save()
#
#             user  = authenticate(username=username, password=password)
#
#             if user is not None:
#                 if user.is_active:
#                     login(request,user)
#                     return redirect('kbstack:index')
#                 else:
#                     return render(request, 'kbstack/login.html', {'error_message': 'Invalid Credential'})
#         return render(request,self.template_name,{'form':form})



def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'kbstack/index.html', {'username': username})
            else:
                return render(request, 'kbstack/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'kbstack/login.html', {'error_message': 'Invalid login'})
    return render(request, 'kbstack/login.html', {'username': 'error'})


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'kbstack/login.html', context)