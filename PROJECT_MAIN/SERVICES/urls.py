from django.urls import path
from SERVICES.views import *
from PROJECT_MAIN_APP.views import *

urlpatterns = [
    
    path('',Inicio, name='Inicio'),
    path('Registros/',Registros, name='Registros'),
    path('Eliminar_empleado/<idEmpleado>/', Eliminar_empleado, name='Eliminar_empleado'),
    path('Editar_empleado/', Editar_empleado, name='Editar_empleado'),
    path('Agregar_empleado/', Agregar_Empleado, name='Agregar_Empleado'),
]