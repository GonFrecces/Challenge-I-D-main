from pathlib import Path
from django.urls import path
from PROJECT_MAIN_APP.views import *
from DASHBOARD.views import *
from SERVICES.views import *
from CAPTURERS .views import *

urlpatterns = [
    
    path('',Inicio,name='Inicio'),
    path('Dashboard/',Dashboard, name='DASHBOARD'),
    path('login_user/',login_user, name='LOGIN'),
    path('Registros/',Registros, name='Registros'),
    path('Dispositivos/',Dispositivos, name='Dispositivos'),
    path('Enrolar/',Enrolar, name='Enrolar'),
    path('Marcador/',Marcador, name='Marcador'),
    
]