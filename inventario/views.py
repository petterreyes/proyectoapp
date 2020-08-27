from django.shortcuts import render

# Create your views here.

#pagina inicial del crud SELECT
def docentes(request, template_name="docentes.html"):
    return render(request, template_name)

#pagina de crear o insertar INSERT
def creardocentes(request, template_name="creardocentes.html"):
    return render(request, template_name)

#pagina de modificar o actualizar al docente UPDATE
def modificardocentes(request, template_name="modificardocentes.html"):
    return render(request, template_name)

#pagina de borrado o eliminado al docente DELETE
def eliminardocentes(request, template_name="eliminardocentes.html"):
    return render(request, template_name)