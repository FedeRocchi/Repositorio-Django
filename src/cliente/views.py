from django.shortcuts import render

# Create your views here.
from .models import Cliente

def ver_cliente(request):
    cliente = Cliente.objects.all()
    return render(request, 'cliente/index.html', {'clientes': cliente})