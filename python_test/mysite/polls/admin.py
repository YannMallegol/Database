from django.contrib import admin

# Register your models here.
from .models import Question, Choice, Key, MR_Params,US_Params,CT_Params,Review

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Key)
admin.site.register(MR_Params)
admin.site.register(US_Params)
admin.site.register(CT_Params)
admin.site.register(Review)