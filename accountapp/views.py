from audioop import reverse

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView, DetailView

from accountapp.models import helloWorld
from django.urls import reverse, reverse_lazy


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

class AccountCreateView(CreateView):
    model = User #장고 기본 제공 모델
    form_class = UserCreationForm #장고 기본 제공 폼
    success_url = reverse_lazy('accountapp:helloworld') #reverse 함수형 reverse_lazy 클래스형
    template_name = 'accountapp/create.html'

class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'