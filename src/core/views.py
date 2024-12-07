from django.http import HttpResponse
from django.shortcuts import render


def saludar(request):
    return HttpResponse("Hola desde Django!")
# Create your views here.

def saludar_con_etiqueta(request):
    return HttpResponse("<h1>Este es Titulo de mi App</h1>")

def saludar_con_parametros(request, nombre: str, apellido: str):  
        nombre = nombre.capitalize()
        apellido = apellido.capitalize()
        return HttpResponse(f"{apellido}, {nombre}")

def index(request):
     context = {'año': 2024}
     return render(request,'core/index.html', context)

def tirar_dados(request):
     from datetime import datetime
     from random import randint

     tiro_dados = randint(1,6)
     if tiro_dados == 6:
          mensaje = f'Has tirado el dado y ha sacado {tiro_dados} GANASTE!'
     else:
          mensaje = f'Has tirado el dado y sacaste {tiro_dados}, Perdiste. Intenta nuevamente, aprete F5'
    
     datos = {'title': 'tiro de Dados', 
              'mensaje': mensaje,
              'fecha': datetime.now()
              }
     return render(request, 'core/dados.html', context=datos)

def nombre_apellido(request):
    
     while True:
          
          nombre = input("Ingrese su nombre: ")
          apellido = input("Ingrese su apellido: ")

          if not nombre.isalpha and not apellido.isalpha:
               continue
          else:
               mensaje = {'nombre':nombre,
                          'apellido': apellido}
             
               return render(request, 'core/template.html', context=mensaje)
          
def ver_nota(request):
     lista_notas = [3,5,7,8,2,12,5]

     return render(request,'core/bucles.html', {'notas': lista_notas})

          
