from django.urls import path
<<<<<<< HEAD
from accountapp.views import index

app_name = 'accountapp'
urlpatterns = [
    path('index/', index, name='index'),
=======
from . import views

app_name = "accountapp"

urlpatterns = [
    path('', views.helloWorld, name='helloWorld'),
>>>>>>> c443512b1c8b81232a09a87d27a4dbb1acd25f16
]
