from django.urls import path
from . import views 


urlpatterns = [
    path("ensure", views.ensure, name="ensure"),
    path("init", views.init, name="init"),
]


