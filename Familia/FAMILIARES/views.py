from django.shortcuts import render
from FAMILIARES.models import Familia

# Create your views here.

def mostrarFamilia(request):

    familiares = Familia.objects.all ()

    contexto = {

        'familiares':familiares

    }

    return render(request,'familia.html',contexto )