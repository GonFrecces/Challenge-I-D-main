from rest_framework import viewsets
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from CAPTURERS.models import Enrollers, Markers
from SERVICES.models import registro
from .serializers import EnrollersSerializers, MarkersSerializers, RegistrosSerializers

# Create your views here.
#EndPoint Enrollers ===> captura de foto

class EnrollersViewsets(viewsets.ViewSet):
    serializer_class = EnrollersSerializers
    queryset = Enrollers.objects.all()
    def get(self, request, **args):
        queryset = Enrollers.objects.all()
        serializer = EnrollersSerializers(queryset, many=True)
        if queryset.count() > 0:
            return Response(serializer.data)
        else:
            return Response(data = {'Mensaje': 'No existen datos!'})
    
    def retrieve(self, request ,pk=None):
        queryset = Enrollers.objects.all()
        enrollers = get_object_or_404(queryset, pk=pk)
        serializer = EnrollersSerializers(enrollers)
        return Response(serializer.data)

    
    def create(self, request):
        print("llego")
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            print(validated_data)         
            serializer.save()
            return Response({'Mensaje': 'Usuario enrolado exitosamente!'})
        else:
            print(serializer)
            print(serializer.errors)
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
    def destroy(self,request, pk=None):
        if pk is not None:
            enroller = Enrollers.objects.filter(id_enrollers = pk)
            enroller.delete()
            return Response({'Mensaje': 'Enrolamiento eliminado exitosamente!'})
        else:
            return Response({'Mensaje': 'Datos del enrolamiento no existen!'})
    
    def update(self, request, *args, **kwargs):
        instance = self.queryset.get(pk=kwargs.get('pk'))
        serializer = self.serializer_class(instance, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'Mensaje': 'Datos del enrollamiento actualizados exitozamente!'})
        else:
            return Response({'Mensaje': 'Datos del usuario no se han podido actualizar!'})
        
        
#EndPoint Resgistro empleados 
class RegistroViewsets(viewsets.ViewSet):
    serializer_class = RegistrosSerializers
    queryset = registro.objects.all()
    
    def get(self, request, **args):
        queryset = registro.objects.all()
        serializer = RegistrosSerializers(queryset, many=True)
        if queryset.count() > 0:
            return Response(serializer.data)
        else:
            return Response(data = {'Mensaje': 'No existen datos!'})
    
    def retrieve(self, request, pk=None):
        queryset = registro.objects.all()
        registros = get_object_or_404(queryset, pk=pk)
        serializer = RegistrosSerializers(registros)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Mensaje': 'Datos del usuario ingresados exitosamente!'})
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        if pk is not None:
            register = registro.objects.filter(id_register = pk)
            register.delete()
            return Response({'Mensaje': 'Datos del usuario eliminados exitosamente!'})
        else:
            return Response({'Mensaje': 'Datos del usuario no existen!'})


    def update(self, request, *args, **kwargs):
        instance = self.queryset.get(pk=kwargs.get('pk'))
        serializer = self.serializer_class(instance, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'Mensaje': 'Datos del usuario actualizados exitozamente!'})
        else:
            return Response({'Mensaje': 'Datos del usuario no se han podido actualizar!'})

#EndPoint Markers de empleados ==> captura de foto

class MarkerViewsets(viewsets.ViewSet):
    serializer_class = MarkersSerializers
    queryset = Markers.objects.all()
    
    def get(self, request, **args):
        queryset = Markers.objects.all()
        serializer = MarkersSerializers(queryset, many=True)
        if queryset.count() > 0:
            return Response(serializer.data)
        else:
            return Response(data = {'Mensaje': 'No existen datos!'})
    
    def retrieve(self, request, pk=None):
        queryset = Markers.objects.all()
        markers = get_object_or_404(queryset, pk=pk)
        serializer = MarkersSerializers(markers)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Mensaje': 'Marcación ingresada exitosamente!'})
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        if pk is not None:
            markers = Markers.objects.filter(id_markers = pk)
            markers.delete()
            return Response({'Mensaje': 'Marcación de usuario eliminados exitosamente!'})
        else:
            return Response({'Mensaje': 'Datos de la marcacion no existen!'})
    
    