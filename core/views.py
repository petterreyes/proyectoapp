from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import MedicosForm, Medicos

'''from django.shortcuts import render, HttpResponse


# Create your views here.
html_base = """
    <h1>Mi Primer Menu</h1>
    <ul>
        <li>   <a href="/">Portada</a>              </li>
        <li>   <a href="/about-me/">Acerca de</a>   </li>
        <li>   <a href="/contact/">Contacto</a>     </li>
    </ul>
"""

# Create your views here.



#template tag
#block conten
# extends
# url


def home(request):
    html_responsde = "<h1>la pagina de portada</h1>"
    html_responsde = html_base + html_responsde
    return HttpResponse(html_responsde);

def about(request):
    html_responsde = "<h1>la pagina de Acerca De</h1>"
    html_responsde = html_base + html_responsde
    return HttpResponse(html_responsde);

def contact(request):
    html_responsde = "<h1>la pagina de contacto</h1>"
    html_responsde = html_base + html_responsde
    return HttpResponse(html_responsde);
    '''

def home(request, plantilla="home.html"):
    return render(request, plantilla)

def about(request, plantilla="about.html"):
    return render(request, plantilla)

def contact(request, plantilla="contact.html"):
    return render(request, plantilla)

def promociones(request, plantilla="promociones.html"):
    return render(request, plantilla)

def citas(request, plantilla="citas.html"):
    return render(request, plantilla)



def servicios(request, plantilla="servicios.html"):
    return render(request, plantilla)




# Create your views here.

#pagina inicial del crud SELECT
def medico(request, plantilla="medico.html"):
    medicos = Medicos.objects.all()
    data = {
        'medico':medicos
    }
    return render(request, plantilla, data)

#pagina de crear o insertar INSERT
def crearmedicos(request, template_name="crearmedicos.html"):

    if request.method == "POST":
        form = MedicosForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('medico')
    else:
        form = MedicosForm

    return render(request, template_name, {'medico':form})

## MODIFICAR DOCENTE CRUD
def modificarmedicos(request, pk, plantilla="modificarmedicos.html"):
    if request.method == "POST":
        form = MedicosForm(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect('medico')
    else:
        medico = get_object_or_404(Medicos, pk=pk)
        form = MedicosForm(request.POST or None, instance=medico)
    return render(request, plantilla, {'medico': form})


#pagina de borrado o eliminado al medico DELETE
def eliminarmedicos(request, template_name="eliminarmedicos.html"):
    if request.method == "POST":
        form = MedicosForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('medico')
    else:
        form=MedicosForm
    return render(request, template_name, {'medico':form})
