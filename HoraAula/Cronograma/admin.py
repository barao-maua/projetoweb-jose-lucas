from django.contrib import admin
from . import models

#Superadmin
#user: admin
#senha: admin

# Register your models here.
admin.site.register(models.Professor)
admin.site.register(models.Materia)
admin.site.register(models.Horario)
