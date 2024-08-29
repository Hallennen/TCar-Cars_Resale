from django.shortcuts import render, redirect   
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from accounts.forms import UserModelForms

# Create your views here.

def register_view(request):

    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        pessoal_form = UserModelForms(request.POST)
        print(request.POST)

        if user_form.is_valid():
            user_form.save()
            pessoal_form.save()
            return redirect('login')
        
    else:
        user_form = UserCreationForm()
        pessoal_form = UserModelForms()
        print('form_invalid')
        
    return render(request, 'register.html', {'user':{'user_form': user_form},'pessoal':{'pessoal_form': pessoal_form}})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('cars_list')
        else:
            login_form = AuthenticationForm()
    else:
        login_form = AuthenticationForm()



    
    return render(request, 'login.html', {'login_form': login_form})


def logout_views(request):
    logout(request)
    return redirect('login')
    