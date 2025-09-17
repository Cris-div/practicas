from django.urls import path
from . import views

urlpatterns = [
    
    path("productos/", views.listar_productos, name="listar_productos"),
    path("productos/crear/", views.crear_producto, name="crear_producto"),
    path("productos/editar/<int:id>/", views.editar_producto, name="editar_producto"),
    path("productos/eliminar/<int:id>/", views.eliminar_producto, name="eliminar_producto"),
    path("productos/buscar/", views.buscar_producto, name="buscar_producto"),

    path("proveedores/", views.listar_proveedores, name="listar_proveedores"),
    path("proveedores/crear/", views.crear_proveedor, name="crear_proveedor"),
    path("proveedores/editar/<int:id>/", views.editar_proveedor, name="editar_proveedor"),
    path("proveedores/eliminar/<int:id>/", views.eliminar_proveedor, name="eliminar_proveedor"),
]
