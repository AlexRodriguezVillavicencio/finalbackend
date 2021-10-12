from django.urls import path
from . import views

app_name = 'tienda'

urlpatterns = [
    path('',views.index,name='index'),
    



    
    path('agregarCarrito/<int:producto_id>',views.agregarCarrito,name='agregarCarrito'),
    path('carrito',views.carrito,name='carrito'),
    path('eliminarProductoCarrito/<int:producto_id>',views.eliminarProductoCarrito,name="eliminarProductoCarrito"),
    path('limpiarCarrito',views.limpiarCarrito,name='limpiarCarrito'),


    #path('pedido',views.pedido,name='pedido'),

    #path('pagoexitosopaypal',views.pago_exitoso_paypal,name='pagoexitosopaypal'),



    path('categoria/<slug>/',views.categoria, name="categoria"),
    path('producto/<slug>/',views.producto,name='producto'),

]