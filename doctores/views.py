from django.shortcuts import render, redirect
from .forms import MedicosForm

# Create your views here.

#pagina inicial del crud SELECT
def medicos(request, template_name="medico.html"):
    return render(request, template_name)

#pagina de crear o insertar INSERT
def crearmedicos(request, template_name="crearmedicos.html"):

    if request.method == "POST":
        form = MedicosForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('medico')

    return render(request, template_name, {'medico':form})

#pagina de modificar o actualizar al medico UPDATE
def modificarmedicos(request, template_name="modificarmedicos.html"):
    return render(request, template_name)

#pagina de borrado o eliminado al medico DELETE
def eliminarmedicos(request, template_name="eliminarmedicos.html"):
    return render(request, template_name)