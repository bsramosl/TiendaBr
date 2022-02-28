
from re import template
from .models import *
from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView, RedirectView,DetailView
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from .forms import *
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib.auth import login, logout, update_session_auth_hash
from django.http import HttpResponseRedirect, request, HttpResponse, JsonResponse
 

class Index(ListView):
    model = Producto
    template_name = 'Index.html' 
     

class Registro(CreateView):
    model = User
    form_class = UsuarioForm
    template_name = 'Registro.html'
    success_url = reverse_lazy('Tienda:Index') 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registrar Usuario'
        return context

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return self.render_to_response(
            self.get_context_data(request=self.request, form=form))

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Se ha registrado con exito')
        return response



class Login(FormView):
    template_name = 'Login.html'
    form_class = LoginForm
    success_url = reverse_lazy('Tienda:Index')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs) 

    def form_valid(self, form):
        login(self.request, form.get_user())
        messages.success(self.request, 'Bienvenido')
        return super(Login, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return self.render_to_response(
            self.get_context_data(request=self.request, form=form))


class LogoutUsuario(RedirectView):
    pattern_name = 'Tienda:Index'

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super().dispatch(request, *args, **kwargs)


class RegistroProducto(CreateView):
    model = Producto
    form_class =  ProductoForm
    template_name = 'RegistroProducto.html'
    success_url = reverse_lazy('Tienda:Index')  

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return self.render_to_response(
            self.get_context_data(request=self.request, form=form))

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Se ha registrado con exito')
        return response
 

class Productos(DetailView):
    model = Producto
    template_name = 'Producto.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['book_list'] = Producto.objects.all()
        return context

class ActualizarProducto(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'ActualizarProducto.html'
    success_url = reverse_lazy('Tienda:Index')

class DeleteProducto(DeleteView):
    model = Producto
    template_name = 'DeleteProducto.html'
    success_url = reverse_lazy('Tienda:Index')

    
class ListarProducto(ListView):
    model = Producto
    template_name = 'ListadoProducto.html'