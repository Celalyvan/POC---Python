from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from personas.models import Persona


def bienvenido(request):
    nro_personas = Persona.objects.count() # hace la conexion a la bdd
    # personas = Persona.objects.all()
    personas = Persona.objects.order_by('id')
    return render(request, 'bienvenido.html', {'nro_personas':nro_personas, 'personas':personas})





