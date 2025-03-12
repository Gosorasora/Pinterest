from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def helloworld(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    if request.method == "POST":
        return render(request, "accountapp/helloworld.html", context={"text": "POST World!!"})

    else:
        return render(request, "accountapp/helloworld.html", context={"text": "GET World!!"})