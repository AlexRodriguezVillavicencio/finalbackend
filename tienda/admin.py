from django.contrib import admin
from .models import  Categoria,BebidaVariation,PostreVariation,Producto, OrderItem, Order



admin.site.register(Categoria)
admin.site.register(BebidaVariation)
admin.site.register(PostreVariation)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('pk','nombre','categoria','precio','stock')
    list_display_links = ('pk','nombre')
    list_editable = ('categoria','precio','stock')
    search_fields = ['nombre']
    

admin.site.register(Order)
admin.site.register(OrderItem) 
