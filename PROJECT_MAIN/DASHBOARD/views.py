from http.client import HTTPResponse
from re import L
from urllib import response
from django.shortcuts import render, redirect
from json import JSONDecodeError
from CAPTURERS.models import Enrollers
from django.http import JsonResponse
from django.core import serializers
import requests
import json

# Create your views here.

def Dashboard(request):
    return render(request,"Dashboard/dashboard.html")


def Listado_empleado(request):
    try:
        responses = requests.get("http://127.0.0.1:8000/api/registro/")
        responses_enrolar = requests.get("http://127.0.0.1:8000/api/enrolar/")
        context = {
            'empleados': responses,
            'enrolado': responses_enrolar
            }
        for i in responses.json():
            if i == "Mensaje":
                return render(request,"Dashboard/listado_empleado.html")
            else: 
                context = {
                    'empleados': responses.json()
                }
                return render(request, "Dashboard/listado_empleado.html",context)
    except JSONDecodeError as e:
        print(e)
        return render(request, "Dashboard/listado_empleado.html")
    
def Listar_marcaciones(request):
    try:
        responses = requests.get("http://127.0.0.1:8000/api/registro/")
        responses_marcadores = requests.get("http://127.0.0.1:8000/api/marcadores/")
        context = {
            'empleados': responses,
            'marcadores': responses_marcadores
            }
        for i in responses.json():
            if i == "Mensaje":
                return render(request,"Dashboard/listado_marcaciones.html.html")
            else: 
                context = {
                    'empleados': responses.json(),
                    'marcadores': responses_marcadores.json()
                }
                return render(request, "Dashboard/listado_marcaciones.html",context)
    except JSONDecodeError as e:
        print(e)
        return render(request, "Dashboard/listado_marcaciones.html.html")

def image_empleado(request):
    id_empleado = request.POST.get('id')
    print(id_empleado)
    imagen = Enrollers.objects.filter(id_enrollers = id_empleado).values_list()

    if imagen:
        print(imagen)
        data = {'data':list(imagen)}
        return JsonResponse(data)
        
    
    