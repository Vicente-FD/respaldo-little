from django.shortcuts import render, redirect
from .models import *
import os
from django.conf import settings
# Create your views here.

def cargarIndex(request):
    return render(request, "index.html")

def cargarCarrito(request):
    return render(request, "carrito2.html")

def cargarSuscripcion(request):
    return render(request, "suscripcion.html")

def cargarNosotras(request):
    return render(request, "nosotras.html")

def cargarTerms(request):
    return render(request, "terms.html")

def agregarProducto(request):
    return render(request, "agregarProducto.html")

def CargarAgregarProducto(request):
    productos = Producto.objects.all()
    categoria = Categoria.objects.all()
    return render(request, "agregarProducto.html", {'prod':productos, 'Categoria':categoria})

def CargarProductosCarrito(request):
    productos = Producto.objects.all()
    categoria = Categoria.objects.all()
    return render(request, "carrito2.html", {'prod':productos, 'Categoria':categoria})

def agregarProducto(request):
    v_sku = request.POST['txtSku'] 
    v_nombre = request.POST['txtNombre']
    v_stock = request.POST['txtStock']
    v_precio = request.POST['txtPrecio']
    if request.POST['fechaVencimientoSel'] == "":
        v_fecha_vencimiento = None
    else:
        v_fecha_vencimiento = request.POST['fechaVencimientoSel']
    v_image = request.FILES['txtImg']

    Producto.objects.create(sku=v_sku, nombreProd=v_nombre,  precio=v_precio, stock=v_stock,  fecha_vencimiento=v_fecha_vencimiento, image_url=v_image)

    return redirect('/agregarProducto')

def cargarEditarProducto(request, sku):
    productos = Producto.objects.get(sku=sku)
    return render(request, "editarProducto.html", {"prod": productos})

def editarProductoForm(request):
    v_sku = request.POST['txtSku']
    productoBD = Producto.objects.get(sku=v_sku)
    v_nombre = request.POST['txtNombre']
    v_stock = request.POST['txtStock']
    v_precio = request.POST['txtPrecio']
    if request.POST['fechaVencimientoSel'] == "":
        v_fecha_vencimiento = None
    else:
        v_fecha_vencimiento = request.POST['fechaVencimientoSel']

    try:
        v_image = request.FILES['txtImg']
        ruta_imagen = os.path.join(
            settings.MEDIA_ROOT, str(productoBD.image_url))
        os.remove(ruta_imagen)
    except:
        v_image = productoBD.image_url

    productoBD.nombreProd = v_nombre
    productoBD.stock = v_stock
    productoBD.precio = v_precio
    productoBD.fecha_vencimiento = v_fecha_vencimiento
    productoBD.image_url = v_image


    productoBD.save()

    return redirect('/agregarProducto')

def eliminarProducto(request,sku):
    productoBD = Producto.objects.get(sku = sku)
    ruta_imagen = os.path.join(settings.MEDIA_ROOT, str(productoBD.image_url))
    os.remove(ruta_imagen)
    productoBD.delete() 
    return redirect('/agregarProducto')

def validarLogin(request):
    v_email = request.POST['form3Example1cg']
    v_password = request.POST['form3Example4cg']

    if v_email == 'admin@correo.com' and v_password == 'contraseñamuysegura':
        request.session['email'] = v_email
        request.session['contraseña'] = v_password
        return redirect('/modoAdmin')

    try:
        usuarioBD = Usuario.objects.get(email=v_email, password=v_password)
        request.session['email'] = usuarioBD.email
        request.session['contraseña'] = usuarioBD.password
        return redirect('/indexSignup')
    except Usuario.DoesNotExist:
        error_message = "Usuario o contraseña incorrectos"
        return render(request, "login.html", {"error_message": error_message})