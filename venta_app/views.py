from django.shortcuts import render, redirect
from .models import Venta

def inicio_vistaVentas(request):
    lasVentas = Venta.objects.all()
    return render(request, "gestionarVentas.html", {"misVentas": lasVentas})

def registrarVenta(request):
    id_venta = request.POST["numIdVenta"]
    nombre = request.POST["txtNombre"]
    hora_compra = request.POST["txtHoraCompra"]
    contenido = request.POST["txtContenido"]
    cantidad = request.POST["numCantidad"]
    total = request.POST["numTotal"]
    nom_cliente = request.POST["txtNomCliente"]
    reg_final= request.POST["numTotal"]

    Venta.objects.create(
        id_venta=id_venta,
        nombre=nombre,
        hora_compra=hora_compra,
        contenido=contenido,
        cantidad=cantidad,
        total=total,
        nom_cliente=nom_cliente,
        reg_final=reg_final
    )

    return redirect("ventas")

def seleccionarVenta(request, id_venta):
    venta = Venta.objects.get(id_venta=id_venta)
    return render(request, "editarVentas.html", {"miVenta": venta})

def editarVenta(request):
    id_venta = request.POST["numIdVenta"]
    nombre = request.POST["txtNombre"]
    hora_compra = request.POST["txtHoraCompra"]
    contenido = request.POST["txtContenido"]
    cantidad = request.POST["numCantidad"]
    total = request.POST["numTotal"]
    nom_cliente = request.POST["txtNomCliente"]
    reg_final= request.POST["numTotal"]

    venta = Venta.objects.get(id_venta=id_venta)
    venta.nombre = nombre
    venta.hora_compra = hora_compra
    venta.contenido = contenido
    venta.cantidad = cantidad
    venta.total = total
    venta.nom_cliente = nom_cliente
    venta.reg_final=reg_final
    venta.save()

    return redirect("ventas")

def borrarVenta(request, id_venta):
    venta = Venta.objects.get(id_venta=id_venta)
    venta.delete()
    return redirect("ventas")
