from json import JSONDecodeError
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Enrollers, Dispositivos
import platform as pl 
import requests
import json
import re, uuid

def Dispositivos_(request):
    dispositivos = Dispositivos.objects.all()
    context = {'data': dispositivos}
    return render(request, "Capturers/dispositivos.html",context)
    
def Enrolar(request):
    return render(request, "Capturers/enrolar.html")

def Marcador(request):
    return render(request, "Capturers/marcador.html")

def Enrolar_empleado(request):
    
    if request.method == "POST":
        sistema_operativo = pl.system()
        mac_address = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
        hostname = pl.node()
        machine = pl.machine()
        processor = pl.processor()
        release = pl.release()
        dispositivos = Dispositivos(
            sistema_operativo=sistema_operativo,
            mac_address=mac_address,
            hostname=hostname,
            machine=machine,
            processor=processor,
            release=release)
        dispositivos.save()
        parametros = {
            'image_enrollers': request.POST.get('image_enrollers'),
            'rut_enrollers': request.POST.get('rut_enrollers')
            }
        responses = requests.post("http://127.0.0.1:8000/api/enrolar/", parametros).json()
        
        return redirect("DASHBOARD:Enrolar_empleado")
    else:    
        return render(request, "Capturers/enrolar.html")
    
def Eliminar_enrolado(request):
    id_enrollers = request.POST.get("id_enrollers")
    empleado = Enrollers.objects.filter(id_enrollers = id_enrollers)
    if empleado is not None:
        responses = requests.delete("http://127.0.0.1:8000/api/enrolar/"+id_enrollers)
        print(responses)
        messages.success(request, "Registro eliminado con exito!")
        return redirect("DASHBOARD:Listado_empleado")
        

    
def Marcar_empleado(request):
    if request.method == "POST":
        parametros = {
            'image_markers': request.POST.get('image_markers'),
            'rut_markers': request.POST.get('rut_markers')
            }
        responses = requests.post("http://127.0.0.1:8000/api/marcadores/", parametros).json()

        return redirect("DASHBOARD:Marcar_empleado")
    else:    
        return render(request, "Capturers/marcador.html")