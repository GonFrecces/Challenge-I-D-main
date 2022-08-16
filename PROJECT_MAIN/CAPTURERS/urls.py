from django.urls import path
from CAPTURERS.views import *
from DASHBOARD.views import Dashboard
from PROJECT_MAIN_APP.views import *

urlpatterns = [
    
    path('Dispositivos/',Dispositivos_, name='Dispositivos'),
    path('Dashboard/',Dashboard, name='Dashboard'),
    path('Enrolar_empleado/',Enrolar_empleado, name='Enrolar_empleado'),
    path('Eliminar_enrolado/',Eliminar_enrolado, name='Eliminar_enrolado'),
    path('Marcar_empleado/',Marcar_empleado, name='Marcar_empleado'),
    path('Enrolar/',Enrolar, name='Enrolar'),
    path('Marcador/',Marcador, name='Marcador'),
    path('',Inicio, name='Inicio'),

    
]