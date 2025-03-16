from audioop import reverse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from accountapp.models import helloWorld
from django.urls import reverse

# Create your views here.

def helloworld(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    if request.method == "POST":

        temp = request.POST.get("helloworld_input")

        new_helloWorld = helloWorld() #helloWorld은 모델
        new_helloWorld.text = temp
        new_helloWorld.save()
        # 모델에 값을 저장 함
        return HttpResponseRedirect(reverse('accountapp:helloworld'))
        # account/helloworld와 같음.
    else:
        helloWorld_list = helloWorld.objects.all()
        return render(request, "accountapp/helloworld.html", context={"helloWorld_list": helloWorld_list})