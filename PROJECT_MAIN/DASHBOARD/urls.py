from django.urls import path
from DASHBOARD.views import *
from SERVICES.views import Editar_empleado
from SERVICES.views import Agregar_Empleado
from SERVICES.views import Registros
from CAPTURERS.views import *
from PROJECT_MAIN_APP.views import logout

urlpatterns = [
    
    path('Dispositivos/',Dispositivos_, name='Dispositivos'),
    path('Dashboard/', Dashboard, name='Dashboard'),
    path('Registros/', Registros, name='Registros'),
    path('Agregar_Empleado/', Agregar_Empleado, name='Agregar_Empleado'),
    path('Editar_empleado/', Editar_empleado, name='Editar_empleado'),
    path('Enrolar_empleado/',Enrolar_empleado, name='Enrolar_empleado'),
    path('Eliminar_enrolado/',Eliminar_enrolado, name='Eliminar_enrolado'),
    path('Marcar_empleado/',Marcar_empleado, name='Marcar_empleado'),
    path('Listado_empleado/',Listado_empleado, name='Listado_empleado'),
    path('Listar_marcaciones/',Listar_marcaciones, name='Listar_marcaciones'),
    path('image_empleado',image_empleado, name='image_empleado'),
    
    
    
    path('',logout, name='Logout'),
    
]