from django.urls import path
from . import views 


urlpatterns = [
    path("ensure", views.ensure, name="ensure"),
    path("config", views.config, name="config"),
    path("init", views.init, name="init"),
    path("add", views.add, name="add"),
    path("commit", views.commit, name="commit"),
    path("pull", views.pull, name="pull"),
]


