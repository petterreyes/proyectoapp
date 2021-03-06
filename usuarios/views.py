'''
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout

# Create your views here.
def login(request, plantilla=usuarios/login.html):
    #creamos el formulario de autenticacion vacio
    form = AuthenticationForm()
    if request.method == "POST":
        #anadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        #SI EL FORMULARIO ES VALIDO
        if form.is_valid():
            #recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            #verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            #si existe un usuario y nombre con esa contrasena
            if user is not None:
                #hacemos el login manualmente
                do_login(request, user)
                #y lo redireccionamos a la portada
                return redirect("home")

    #si llegamos a la final renderizamos el formulario
    '''
    #return render(request, plantilla, {'form',:form})





