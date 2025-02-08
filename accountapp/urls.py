from django.urls import path
from accountapp.views import index

app_name = 'accountapp'
urlpatterns = [
    path('index/', index, name='index'),
]
