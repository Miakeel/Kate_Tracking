from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.

# admin.site.register(Participant)
admin.site.register(QrCodeId)
admin.site.register(Entry)

class ParticipantResource(resources.ModelResource):

    class Meta:
        model = Participant
        fields=('first_name','last_name','institution','email','title','phone','city','country','scfhs_number')

class ParticipantAdmin(ImportExportModelAdmin):
    resource_classes=[ParticipantResource]

admin.site.register(Participant,ParticipantAdmin)