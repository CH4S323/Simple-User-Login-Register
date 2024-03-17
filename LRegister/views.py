from django.shortcuts import render, redirect
from .models import User
from .forms import UserCreateForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def RegisterUser(request):
    print("Sign up")

    form = UserCreateForm()

    if request.method == 'POST':
        email = request.POST.get('email')
        
        try:
            user = User.objects.get(email=email)
            print(user)
        except User.DoesNotExist:
            pwd1 = request.POST.get('password1')
            pwd2 = request.POST.get('password2')
            if pwd1 == pwd2:
                form = UserCreateForm(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('register')
                else:
                    
                    messages.error(request,"Password must not be similar to User name ")    
            else:
                
                messages.error(request,"Password doesnt match ")
                
        else:
            messages.error(request, 'Email already exist!')
            return redirect('register')

    context = {
        'form': form,
    }
    return render(request, 'LoginRegister.html', context)

def LoginUser(request):
    print("Login")
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('pswd')
        
        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, "Email doesn't exist")
        
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('temp')
        else:
            messages.error(request, 'Wrong Password')

    return render(request, 'LoginRegister.html')


def temp(request):
    return render(request, 'temp.html')    

def logoutUser(request):
        logout(request)
        return redirect('temp')