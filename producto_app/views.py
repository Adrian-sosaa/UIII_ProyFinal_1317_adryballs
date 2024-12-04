from django.shortcuts import render, redirect
from .models import Producto

def inicio_vistaProductos(request):
    losProductos = Producto.objects.all()
    return render(request, "gestionarProductos.html", {"misProductos": losProductos})

def registrarProducto(request):
    codigo = request.POST["numCodigo"]
    nombre = request.POST["txtNombre"]
    precio = request.POST["numPrecio"]
    direccion = request.POST["txtDireccion"]
    destinatario = request.POST["txtDestinatario"]
    cant_producto = request.POST["numCantidad"]
    calidad = request.POST["txtCalidad"]
    id_sucursal = request.POST["txtsucursal"]
    id_prov = request.POST["txtprov"]
    stock = request.POST["numstock"]

    Producto.objects.create(
        codigo=codigo,
        nombre=nombre,
        precio=precio,
        direccion=direccion,
        destinatario=destinatario,
        cant_producto=cant_producto,
        calidad=calidad,
        id_sucursal=id_sucursal,
        id_prov=id_prov,
        stock=stock,
    )

    return redirect("productos")

def seleccionarProducto(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    return render(request, "editarProductos.html", {"miProducto": producto})

def editarProducto(request):
    codigo = request.POST["numCodigo"]
    nombre = request.POST["txtNombre"]
    precio = request.POST["numPrecio"]
    direccion = request.POST["txtDireccion"]
    destinatario = request.POST["txtDestinatario"]
    cant_producto = request.POST["numCantidad"]
    calidad = request.POST["txtCalidad"]
    id_sucursal = request.POST["txtsucursal"]
    id_prov = request.POST["txtprov"]
    stock = request.POST["numstock"]

    producto = Producto.objects.get(codigo=codigo)
    producto.nombre = nombre
    producto.precio = precio
    producto.direccion = direccion
    producto.destinatario = destinatario
    producto.cant_producto = cant_producto
    producto.calidad = calidad
    producto.id_sucursal = id_sucursal
    producto.id_prov = id_prov
    producto.stock = stock
    producto.save()

    return redirect("productos")

def borrarProducto(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    producto.delete()
    return redirect("productos")