from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def Inicio(request):
    return render(request,"Inicio/inicio.html")

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        print('si hace login')
        user = authenticate(username=username, password=password)
        print(user)
        if user :
            login(request, user)
            return redirect('PROJECT_MAIN_APP:DASHBOARD')
        else:
            messages.warning(request, "Correo o contrasena invalidas")
            return render(request, "Inicio/index.html")

    else:
        return render(request,"Inicio/index.html")

def user_logout(request):
    logout(request)
    return redirect('/')