from django.contrib import admin

# Register your models here.

from .models import *

#admin.site.register(MagazineDetails)

@admin.register(MagazineDetails)
class ModelMagazineDetails( admin.ModelAdmin ):

    list_display = ( 'year' , 'title' , 'editor_name')