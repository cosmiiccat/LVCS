from django.urls import path
from . import views 


urlpatterns = [
    path("ensure", views.ensure, name="ensure"),
    path("config", views.config, name="config"),
    path("init", views.init, name="init"),
    path("add", views.add, name="add"),
    path("commit", views.commit, name="commit"),
    path("pull", views.pull, name="pull"),
<<<<<<< HEAD
=======
    path("push", views.push, name="push"),
>>>>>>> 077cfe0e4ba0521a475c4bb81164fc0a3ce6b7ee
]


