from django.contrib import admin

from .models import Group,Tag,User,Feed,Patient,Study,Data,Series,MR_Params,US_Params,CT_Params,Review,Token

admin.site.register(Group)
admin.site.register(Tag)
admin.site.register(User)
admin.site.register(Feed)
admin.site.register(Patient)
admin.site.register(Study)
admin.site.register(Data)
admin.site.register(Series)
admin.site.register(MR_Params)
admin.site.register(US_Params)
admin.site.register(CT_Params)
admin.site.register(Review)
admin.site.register(Token)
