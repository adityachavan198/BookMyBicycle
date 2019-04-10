from django.contrib import admin
from .models import *



class StandAdmin(admin.ModelAdmin):#used to display the title as well as other attributes of the book
    # fields=['sid','sstate','scity','sloc']
    list_display=['sid','sstate','scity','sloc']
    search_fields=['sid','sstate','scity','sloc'] #to add search fields
    list_filter=['sstate','scity'] #to add filter functionality

class CycleAdmin(admin.ModelAdmin):#used to display the title as well as other attributes of the book
    #fields=['cid','cstate','sid']
    list_display=['cid','cstate','sid']
    search_fields=['cid','cstate','sid'] #to add search fields


class UserAdmin(admin.ModelAdmin):
    list_display=['id','first_name','last_name','email']

class BookAdmin(admin.ModelAdmin):
    #fields=['bid','cid','sid_end','sid_start','uid']
    list_display=['bid','cid','sid_end','sid_start','uid']
    search_fields=['bid','uid','cid'] #to add search fields
    list_filter=['uid','cid'] #to add filter functionality

# Register your models here.
admin.site.register(UserOfApp,UserAdmin)
# admin.site.register(LogOfApp)
admin.site.register(Stand,StandAdmin)
admin.site.register(Cycle,CycleAdmin)
admin.site.register(Book,BookAdmin)
admin.site.site_header = "Library Admin"
admin.site.site_title = "Admin Page"
admin.site.index_title = "BookMyCycle Admin Page"
