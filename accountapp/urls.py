from django.urls import path
from accountapp.views import helloWorld
from . import views

app_name = "accountapp"
urlpatterns = [
    path('helloWorld', views.helloWorld, name='helloWorld'),
]



