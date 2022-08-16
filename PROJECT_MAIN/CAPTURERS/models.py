from django.db import models
from datetime import datetime
import os


# Create your models here.
class Enrollers(models.Model):
    id_enrollers = models.AutoField(primary_key=True,serialize=True, verbose_name='id_enrollers')
    image_enrollers = models.ImageField(upload_to='media/Images_enrollers/%y',null=True, blank=True,verbose_name="image_enrollers")
    rut_enrollers = models.CharField(max_length=100, blank=True, null=True)
    
    def delete(self, *args, **kwargs):
        if os.path.isfile(self.image_enrollers.path):
            os.remove(self.image_enrollers.path)
        super(Enrollers, self).delete(*args, **kwargs)
        
    def __str__(self):
        return '%s,%s,%s' %(self.id_enrollers,self.image_enrollers,self.rut_enrollers)



class Markers(models.Model):
    id_markers = models.AutoField(primary_key=True,serialize=True, verbose_name='id_marker')
    image_markers = models.ImageField(upload_to='media/Images_markers/%y',null=True, blank=True,verbose_name="image_markers")
    fecha_markers = models.DateField(default=datetime.now)
    rut_markers = models.CharField(max_length=100, blank=True, null=True)
    
    def delete(self, *args, **kwargs):
        if os.path.isfile(self.image_markers.path):
            os.remove(self.image_markers.path)
        super(Markers, self).delete(*args, **kwargs)
        
    def __str__(self):
        return '%s,%s,%s' %(self.id_markers,self.image_markers,self.rut_markers)
    

class Dispositivos(models.Model):
    id_dispositivo = models.AutoField(primary_key=True,serialize=True, verbose_name='id_dispositivo')
    sistema_operativo = models.CharField(max_length=100, blank=True, null=True)
    mac_address = models.CharField(max_length=100, blank=True, null=True)
    hostname = models.CharField(max_length=100, blank=True, null=True)
    machine = models.CharField(max_length=100, blank=True, null=True)
    processor = models.CharField(max_length=100, blank=True, null=True)
    release = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return '%s,%s,%s,%s,%s,%s,%s' %(self.id_dispositivo,self.sistema_operativo,self.mac_address,self.hostname,self.machine,self.processor,self.release)