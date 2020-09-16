from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def mi_funcion(request):
    return render(request, 'hola_mundo.html')