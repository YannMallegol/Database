from django.contrib import admin

# Register your models here.
from .models import Patient, Study, Series, MR_Params,US_Params,CT_Params,Review

admin.site.register(Patient)
admin.site.register(Study)
admin.site.register(Series)
admin.site.register(MR_Params)
admin.site.register(US_Params)
admin.site.register(CT_Params)
admin.site.register(Review)










