from django.contrib import admin
from .models import *



class StandAdmin(admin.ModelAdmin):#used to display the title as well as other attributes of the book
    fields=['sid','sstate','scity','sloc']
    list_display=['sid','sstate','scity','sloc']
    search_fields=['sid','sstate','scity','sloc'] #to add search fields
    list_filter=['sstate','scity'] #to add filter functionality

# Register your models here.
admin.site.register(UserOfApp)
# admin.site.register(LogOfApp)
admin.site.register(Stand,StandAdmin)
admin.site.register(Cycle)
admin.site.register(Book)
admin.site.site_header = "Library Admin"
admin.site.site_title = "Admin Page"
admin.site.index_title = "BookMyCycle Admin Page"
