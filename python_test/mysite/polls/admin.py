from django.contrib import admin

# Register your models here.
from .models import Patient,Study,Series,MR_Params,US_Params,CT_Params,Review

class StudyInline(admin.TabularInline):
    model = Study



class PatientAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['PatientName']}),
        ('Patient information', {'fields': ['PatientID', 'PatientAge', 'PatientSex', 'PatientBirthDate'],
        'classes': ['collapse']},
        ),
    ]

    inlines = [StudyInline]
    list_display = ('PatientName', 'PatientID', 'PatientAge', 'PatientSex', 'PatientBirthDate')
    search_fields = ['PatientName', 'PatientID', 'PatientAge', 'PatientSex', 'PatientBirthDate']


class SeriesInline(admin.TabularInline):
    model = Series

class SeriesAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['SeriesInstanceUID']}),
        ( 'Series information', {'fileds':['SeriesNumber','SeriesInstanceUID', 'ProtocolName', 'Modality',
         'SeriesDescription', 'SeriesTime', 'ContrastAgent','ScanningSequence','BodyPartExaminated','AcquisitionNumber'],
         'classes': ['collapse']},
         ),
    ]
    list_display = ('SeriesInstanceUID','SeriesNumber','SeriesInstanceUID', 'ProtocolName', 'Modality','SeriesDescription', 'SeriesTime', 'ContrastAgent','ScanningSequence','BodyPartExaminated','AcquisitionNumber')
    search_fields = ['SeriesInstanceUID','SeriesNumber','SeriesInstanceUID', 'ProtocolName', 'Modality','SeriesDescription', 'SeriesTime', 'ContrastAgent','ScanningSequence','BodyPartExaminated','AcquisitionNumber']


class StudyAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['StudyDescription']}),
        ('Study information', {'fields': ['StationName', 'ManufacturerModelName', 'StudyInstanceUID', 'Pathology',
        'StudyDate', 'StudyTime', 'AccessionNumber', 'InstitutionName', 'ReferringPhysicianName',
        'PerformingPhysicianName', 'ModalitiesInStudy'],
        'classes': ['collapse']},
        ),
    ]

    inlines = [SeriesInline]
    list_display = ('StudyDescription', 'StationName', 'ManufacturerModelName', 'StudyInstanceUID', 'Pathology',
    'PerformingPhysicianName', 'ModalitiesInStudy')
    search_fields = ['StudyDescription', 'StationName', 'ManufacturerModelName', 'StudyInstanceUID', 'Pathology',
    'PerformingPhysicianName', 'ModalitiesInStudy']

admin.site.register(Patient, PatientAdmin)
admin.site.register(Study, StudyAdmin)
admin.site.register(Series)
admin.site.register(MR_Params)
admin.site.register(US_Params)
admin.site.register(CT_Params)
admin.site.register(Review)
