from django.urls import path
from PrincipalApp import views
from django.contrib.auth.decorators import login_required

app_name = 'Tienda'
urlpatterns = [
   path('',  views.Index.as_view(), name='Index'), 
   path('Index/',views.Index.as_view(), name='Index'),
   path('Login/',views.Login.as_view(), name='Login'),
   path('Registro/',views.Registro.as_view(), name='Registro'),
   path('Logout/',views.LogoutUsuario.as_view(), name='Logout'),
   path('ListarProducto/',views.ListarProducto.as_view(), name='ListarProducto'),
   path('RegistroProducto/',views.RegistroProducto.as_view(), name='RegistroProducto'),
   path('Producto/<int:pk>/',views.Productos.as_view(), name='Producto'),
   path('UpdateProducto/<int:pk>/',views.ActualizarProducto.as_view(), name='UpdateProducto'),
   path('DeleteProducto/<int:pk>/',views.DeleteProducto.as_view(), name='DeleteProducto'),

   path('RegistrarCategoria/',views.RegistrarCategoria.as_view(), name='RegistrarCategoria'),
   path('ListarCategoria/',views.ListarCategoria.as_view(), name='ListarCategoria'),
   path('UpdateCategoria/<int:pk>/',views.ActualizarCategoria.as_view(), name='UpdateCategoria'),
   path('DeleteCategoria/<int:pk>/',views.DeleteCategoria.as_view(),name='DeleteCategoria'),
 

   path('ListarCarrito/',views.ListarCarrito.as_view(),name='ListarCarrito'),

]