from django.contrib import admin

from myapp.models import *

class PatientsAdmin(admin.ModelAdmin):
    list_display = ('date', 'first_name','last_name','email')

admin.site.register(Patients,PatientsAdmin)
