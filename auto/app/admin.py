from django.contrib import admin
from .models import Colour, Brand, Car

class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('name',)
    search_fields = ('id', 'name')

class ColourAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('name',)
    search_fields = ('id', 'name')



class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'model', 'colour', 'brand', 'price', 'price_types')
    list_filter = ('brand', 'colour')
    search_fields = ('id', 'model', 'brand')

admin.site.register(Brand, BrandAdmin)
admin.site.register(Colour, ColourAdmin)
admin.site.register(Car, CarAdmin)
