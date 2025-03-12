from django.urls import path
from . import views

app_name = "accountapp"
urlpatterns = [
    path('helloworld/', views.helloworld, name='helloworld'),

]



