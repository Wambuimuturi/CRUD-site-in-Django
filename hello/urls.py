from django.urls import path
from . import views
from django.views.generic import TemplateView
#from django.contrib.auth import views as auth_views


app_name = 'hello'
urlpatterns = [
   #path('', TemplateView.as_view(template_name='hello/main.html')),
   path('cookie/', views.cookie, name='cookie-url'),
   path('', views.sessfun, name='session-url'),
]
