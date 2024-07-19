from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from portal_de_salud.models import Medicacion
#from portal_de_salud.forms import FormularioContacto
from portal_de_salud.forms import ContactForm
from portal_de_salud.models import Contact

def profesionales(request):
	return render(request,"profesionales.html")

def contacto(request):
	return render(request,"contacto.html")

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect or show success message here
            return render(request, 'success.html')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def home(request):
	return render(request,"home.html")

def servicios(request):
	return render(request,"servicios.html")

def busqueda_medicacion(request):
	return render(request,"busqueda_medicacion.html")

def buscar(request):
    if request.GET["prd"]:
        producto = request.GET["prd"]
        if len(producto) > 20:
            mensaje = "Texto de búsqueda demasiado largo"
        else:
            articulos = Medicacion.objects.filter(droga__icontains=producto)
            return render(request, "servicios.html", {"articulos": articulos, "query": producto})
    else:
        mensaje = "No has introducido ningún dato"
        return HttpResponse(mensaje)
