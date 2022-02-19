from django.urls import path
from PrincipalApp import views
from django.contrib.auth.decorators import login_required

app_name = 'Tienda'
urlpatterns = [
   path('',  views.Index.as_view(), name='Index'), 
]