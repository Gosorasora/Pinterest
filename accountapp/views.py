<<<<<<< HEAD
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
      return render(request, "accountapp/helloworld.html")
=======
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def helloWorld(request):
  return HttpResponse("Hello World")
>>>>>>> c443512b1c8b81232a09a87d27a4dbb1acd25f16
