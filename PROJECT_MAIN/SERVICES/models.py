from django.db import models
from CAPTURERS.models import Enrollers
# Create your models here.
class registro(models.Model):
    id_register = models.AutoField(primary_key=True,serialize=True,verbose_name='id_register')
    names = models.CharField(max_length=100,blank=True, null=True)
    surnames = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    rut = models.CharField(max_length=12,blank=True, null=True)
    rut_enrollers = models.ForeignKey(Enrollers, on_delete=models.CASCADE, db_column='rut_enrolado')
    
    def __str__(self):
        return '%s,%s,%s,%s,%s,%s' %(self.names,self.surnames,self.email,self.company,self.rut,self.rut_enrollers)