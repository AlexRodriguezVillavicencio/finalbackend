from django.shortcuts import render,reverse, get_object_or_404
from django.conf import settings

from .models import Producto, Categoria
from django.contrib.auth.models import User
from django.db.models import Q
from tienda.carrito import Cart
from .models import Producto, Categoria
from django.views import generic
from .forms import ContactForm, AddToCartForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .utils import get_or_set_order_session



#clase para contacto
# class ContactView(generic.FormView):
#     form_class= ContactForm
#     template_name= 'contacto.html'

#     def get_success_url(self):
#         return reverse("contacto")

#     def form_valid(self,form):
#         messages.info(
#             self.request, "Hemos recibido tu mensaje!")
#         nombre= form.cleaned_data.get('nombre')
#         email= form.cleaned_data.get('email')
#         mensaje= form.cleaned_data.get('mensaje')

#         full_message= f"""
#         Mensaje recibido de {nombre}
#         ______________________________
#         """
#         send_mail(
#             subject="Mensaje recibido por Contact Form",
#             message=full_message,
#             from_email= settings.DEFAULT_FROM_EMAIL,
#             recipient_list=[settings.NOTIFY_EMAIL]
#         )
#         return super(ContactView, self).form_valid(form)


# class ProductListView(generic.ListView):
#     template_name='catalogo.html'
    

#     def get_context_data(self, **kwargs):
#         context = super(ProductListView, self).get_context_data(**kwargs)
#         context.update({
#             "categorias": Categoria.objects.all()
#         })
#         return context



def categoria(request, slug):
    categorias = Categoria.objects.filter(estado = True)
    objCategoria = Categoria.objects.get(slug=slug)
    context = {
        'categorias': categorias,
        'categoria':objCategoria
    }
    return render(request, "categoria.html",context)




def index(request):
    categorias = Categoria.objects.filter(estado = True)
    lista_productos = Producto.objects.all()
    print(settings.MEDIA_URL)
    context = {
        'lstProductos': lista_productos,
        'directorio_img':settings.MEDIA_URL,
        'categorias': categorias,
        }
    return render(request,'index.html',context)








# class ProductDetailView(generic.FormView):
#     template_name = 'producto.html'
#     form_class = AddToCartForm
    
#     def get_object(self):
#         return get_object_or_404(Producto, slug=self.kwargs["slug"])

#     def get_success_url(self):
#         return reverse("tienda:summary")

#     def get_form_kwargs(self):
#         kwargs = super(ProductDetailView, self).get_form_kwargs()
#         kwargs["producto_id"] = self.get_object().id
#         return kwargs

#     def form_valid(self, form):
#         order = get_or_set_order_session(self.request)
#         producto = self.get_object()

#         item_filter = order.items.filter(
#             producto=producto,
#             bebida=form.cleaned_data['bebida'],
#             postre=form.cleaned_data['postre']
#         )

#         if item_filter.exists():
#             item = item_filter.first()
#             item.cantidad += int(form.cleaned_data['cantidad'])
#             item.save()

#         else:
#             new_item = form.save(commit=False)
#             new_item.producto = producto
#             new_item.order = order
#             new_item.save()
        
#         return super(ProductDetailView, self).form_valid(form)

#     def get_context_data(self, **kwargs):
#         context = super(ProductDetailView, self).get_context_data(**kwargs)
#         context['producto'] = self.get_object()
#         return context


def producto(request,slug):
        categorias = Categoria.objects.filter(estado = True)
        objProducto = Producto.objects.get(slug=slug) 
        context = {
            "producto":objProducto,
            'categorias': categorias,
        }
        return render(request,'producto.html',context)





# class CartView(generic.TemplateView):
#     template_name = 'carrito.html'

#     def get_context_data(self, *args, **kwargs):
#         context = super(CartView, self).get_context_data(**kwargs)
#         context["order"] = get_or_set_order_session(self.request)
#         return context





































def agregarCarrito(request,producto_id):
    categorias = Categoria.objects.filter(estado = True)
    objProducto = Producto.objects.get(id=producto_id)
    carritoProducto = Cart(request)
    carritoProducto.add(objProducto,1)
    print(request.session.get("cart"))
    context = {
        "producto":objProducto,
        'categorias': categorias,
    }
    return render(request,'carrito.html',context)

def eliminarProductoCarrito(request,producto_id):
    categorias = Categoria.objects.filter(estado = True)
    objProducto = Producto.objects.get(id=producto_id)
    carritoProducto = Cart(request)
    carritoProducto.remove(objProducto)
    print(request.session.get("cart"))
    context = {
        "producto":objProducto,
        'categorias': categorias,
    }
    return render(request,'carrito.html',context)

def limpiarCarrito(request):
    categorias = Categoria.objects.filter(estado = True)
    CarritoProducto = Cart(request)
    CarritoProducto.clear()
    print(request.session.get("cart"))
    context = {
        'categorias': categorias,
    }
    return render(request,'carrito.html',context)

def carrito(request):
    categorias = Categoria.objects.filter(estado = True)
    print(request.session.get("cart"))
    context = {
        'categorias': categorias,
    }
    return render(request,'carrito.html',context)

# def pedido(request):
#     print(request.user.id)
#     if request.user.id is not None:
#         #SELECCIONAR EL USUARIO
#         userPedido = User.objects.get(id=request.user.id)
#         #SELECCIONAR EL CLIENTE
#         try:
#             clientePedido = Cliente.objects.get(usuario=userPedido)
            
#             nuevoPedido = Pedido()
#             nuevoPedido.cliente = clientePedido
#             nuevoPedido.total = 0
#             nuevoPedido.save()
            
#             pedidoCart = request.session.get("cart")
#             print(pedidoCart)
#             totalPedido = 0
#             lstDetallePedidos = []
#             for key,value in pedidoCart.items():
#                 detalle = PedidoDetalle()
#                 detalle.pedido = nuevoPedido
#                 detalleProducto = Producto.objects.get(id=value["producto_id"])
#                 detalle.producto = detalleProducto
#                 detalle.cantidad = int(value["cantidad"])
#                 detalle.subtotal = float(value["total"])
#                 detalle.save()
#                 lstDetallePedidos.append(detalle)
#                 totalPedido += float(value["total"])
            
#             nuevoPedido.total = totalPedido
#             nuevoPedido.save()
#             ###### PARA PAGO PAYPAL####
#             request.session['paypal_pid'] = nuevoPedido.id
#             host = request.get_host()
#             paypal_datos = {
#                 'business': settings.PAYPAL_RECEIVER_EMAIL,
#                 'amount': nuevoPedido.total,
#                 'item_name': 'PEDIDO #' + str(nuevoPedido.id),
#                 'invoice': str(nuevoPedido.id),
#                 'notify_url': 'http://' + host + '/' + 'paypal-ipn',
#                 'return_url':'http://' + host + '/pagoexitosopaypal'
#             }
#             # formPedidoPaypal = PayPalPaymentsForm(initial=paypal_datos)
#             # context = {
#             #     'pedido' : nuevoPedido,
#             #     'detalles':lstDetallePedidos,
#             #     'formpaypal': formPedidoPaypal
#             # }
#             # return render(request,'pedido.html',context)
#             return render(request,'pedido.html')
#         except:
#             return redirect('/login')
#     else:
#         return redirect('/login')
    
#@login_required
#def logout_view(request):
#    """Logout a user."""
#    logout(request)
#    return redirect('/login')

################# PAYPAL ######################3
# def pago_exitoso_paypal(request):
#     pedido_id = request.session.get('paypal_pid')
#     pedido = Pedido.objects.get(id=pedido_id)
#     pedido.estado = '1'
#     pedido.save()
#     context = {
#      'pedido': pedido   
#     }
#     return render(request,'pagoexitosopaypal.html',context)
    



