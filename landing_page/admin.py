from django.contrib import admin
from landing_page.models import TileModel 


#add columns like this in admin
class IntegratedSupport(admin.ModelAdmin):
    list_display = [field.name for field in TileModel._meta.get_fields()]
    list_filter =('title')
    

admin.site.register(TileModel)


