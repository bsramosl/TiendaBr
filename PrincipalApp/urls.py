from django.urls import path
from PrincipalApp import views
from django.contrib.auth.decorators import login_required

app_name = 'Tienda'
urlpatterns = [
   path('',  views.Index.as_view(), name='Index'),
   path('Index/',  views.Index.as_view(), name='Index'),
   path('Login/', views.Login.as_view(), name='Login'),
   path('Registro/', views.Registro.as_view(), name='Registro'),
   path('Logout/', views.LogoutUsuario.as_view(), name='Logout'),
   path('RegistroProducto/',views.RegistroProducto.as_view(), name='RegistroProducto'),
   path('Producto/<int:pk>/',  views.Producto.as_view(), name='Producto'),
]