from django.shortcuts import render, HttpResponse


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

def medico(request, plantilla="medico.html"):
    return render(request, plantilla)
'''
def Citas(request, plantilla="Citas.html"):
    return render(request, plantilla)
    '''


