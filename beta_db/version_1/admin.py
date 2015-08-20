from django.contrib import admin

# Register your models here.
from .models import Identity, type_of_analyse, age_patient







class IdentityAdmin(admin.ModelAdmin):
	fieldsets = [
		('Date information',               {'fields': ['pub_date']}),
		('Medical record number', {'fields': ['MRN_DBID'], 'classes': ['collapse']}),
	]
	list_display = ('MRN_DBID', 'pub_date')
	list_filter = ['pub_date']
	search_fields = ['MRN_DBID']

admin.site.register(Identity, IdentityAdmin)

class type_of_analyseAdmin(admin.ModelAdmin):
	fieldsets = [
		('diffusion type',               {'fields': ['DIFFUSION']}),
		('MPRAGE',               {'fields': ['MPRAGE']}),
		('localizer', {'fields': ['Localizer'], 'classes': ['collapse']}),
	]
	list_display = ('DIFFUSION', 'Localizer', 'MPRAGE')
	
	search_fields = ['localizer', 'DIFFUSION', 'MPRAGE' ]

admin.site.register(type_of_analyse, type_of_analyseAdmin)




admin.site.register(age_patient)




