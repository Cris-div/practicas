from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Proveedor
from .forms import ProductoForm, ProveedorForm

# ------- Productos -------
def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, "productos/listar.html", {"productos": productos})

def crear_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listar_productos")
    else:
        form = ProductoForm()
    return render(request, "productos/crear.html", {"form": form})

def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect("listar_productos")
    else:
        form = ProductoForm(instance=producto)
    return render(request, "productos/editar.html", {"form": form})

def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == "POST":
        producto.delete()
        return redirect("listar_productos")
    return render(request, "productos/eliminar.html", {"producto": producto})

def buscar_producto(request):
    query = request.GET.get("q")
    resultados = Producto.objects.filter(nombre__icontains=query) if query else []
    return render(request, "productos/buscar.html", {"resultados": resultados})

# ------- Proveedores -------
def listar_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, "proveedores/listar.html", {"proveedores": proveedores})

def crear_proveedor(request):
    if request.method == "POST":
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listar_proveedores")
    else:
        form = ProveedorForm()
    return render(request, "proveedores/crear.html", {"form": form})

def editar_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id=id)
    if request.method == "POST":
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            return redirect("listar_proveedores")
    else:
        form = ProveedorForm(instance=proveedor)
    return render(request, "proveedores/editar.html", {"form": form})

def eliminar_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id=id)
    if request.method == "POST":
        proveedor.delete()
        return redirect("listar_proveedores")
    return render(request, "proveedores/eliminar.html", {"proveedor": proveedor})
