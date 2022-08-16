from django.contrib import admin
from CAPTURERS.models import Enrollers, Markers
from SERVICES.models import registro
# Register your models here.

admin.site.register(Enrollers)
admin.site.register(Markers)
admin.site.register(registro)


