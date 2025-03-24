from django.urls import path
from . import views
from .views import AccountCreateView

app_name = "accountapp"
urlpatterns = [
    path('helloworld/', views.helloworld, name='helloworld'),
    path('create/', AccountCreateView.as_view(), name='create'),

]



