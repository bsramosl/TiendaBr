from multiprocessing import context
from pyexpat import model
from turtle import mode
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
 


class Index(TemplateView):    
    template_name = 'Index.html' 
