from json import JSONDecodeError
from django.shortcuts import render, redirect
from SERVICES.models import registro
from django.contrib import messages
import requests
import json
# Create your views here.
# Vista basada en funciones que entrega a la vista colaboradores un  listado de empleados
def Registros(request):
    try:

        responses = requests.get("http://127.0.0.1:8000/api/enrolar/")
        context = {
            'enrolados': responses
            }
        for i in responses.json():
            if i == "Mensaje":
                return render(request, "Services/registro.html")
            else: 
                context = {
                    'empleados': responses.json()
                }
                return render(request, "Services/registro.html",context)
    except JSONDecodeError as e:
        print(e)
        return render(request, "Services/registro.html")


# Vista basada en funciones que elmina un empleado por id ==> API
def Eliminar_empleado(request, idEmpleado):
    empleado = registro.objects.filter(id_register = idEmpleado)
    if empleado is not None:
        responses = requests.delete("http://127.0.0.1:8000/api/registro/"+idEmpleado)
        print(responses)
        messages.success(request, "Registro eliminado con exito!")
        return redirect("DASHBOARD:Listado_empleado")
# Vista basada en funciones que edita un empleado por id ==> API
def Editar_empleado(request):
    if request.method == 'POST':
        id = request.POST.get('id_edit')
        rut = request.POST.get('rut_edit')
        print(id)
        existe = registro.objects.filter(rut = rut) | registro.objects.filter(id_register = id)
        if  existe:
            parametros = {
                'names': request.POST.get('nombres_edit'),
                'surnames': request.POST.get('apellidos_edit'),
                'email': request.POST.get('correo_edit'),
                'company': request.POST.get('compania_edit'),
                'rut': request.POST.get('rut_edit'),
                'rut_enrollers': request.POST.get('rut_enroller_edit')
            }
            print(parametros)
            responses = requests.put("http://127.0.0.1:8000/api/registro/"+id+"/", parametros).json()
            messages.success(request, "Empleado editado con exito!")
            return redirect("DASHBOARD:Listado_empleado")
        else:
            print('no existe')
            messages.success(request, "Empleado no existe!")
            return redirect("DASHBOARD:Listado_empleado")
    else:    
        return redirect("DASHBOARD:Listado_empleado")
    
#Vista basada en funciones que agrega un emplaedo ==> API
def Agregar_Empleado(request):
    if request.method == 'POST':
        rut_empleado = request.POST.get('rut')
        existe = registro.objects.filter(rut = rut_empleado)
        if  existe:
            print(rut_empleado)
            messages.warning(request, "Empleado ya se encuentra ingresado")
            return redirect("SERVICES:Registros")
        else:
            print('no existe')
            parametros = {
                'names': request.POST.get('nombres'),
                'surnames': request.POST.get('apellidos'),
                'email': request.POST.get('email'),
                'company': request.POST.get('compania'),
                'rut': request.POST.get('rut'),
                'rut_enrollers': request.POST.get('id_empleado')
            }
            print(parametros)
            responses = requests.post("http://127.0.0.1:8000/api/registro/", parametros).json()
            messages.success(request, "Empleado agregado con exito!")
            return redirect("SERVICES:Registros")
    else:    
        
        return redirect("SERVICES:Registros")