from audioop import reverse

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.decorators import account_ownership_required
from accountapp.models import helloWorld
from django.urls import reverse, reverse_lazy

#Decorator List.
has_ownership = [account_ownership_required, login_required]

@login_required
def helloworld(request):
    if request.method == "POST":
        temp = request.POST.get("helloworld_input")
        new_helloWorld = helloWorld()  # helloWorld은 모델
        new_helloWorld.text = temp
        new_helloWorld.save()

        # 모델에 값을 저장 함
        return HttpResponseRedirect(reverse('accountapp:helloworld'))
        # account/helloworld와 같음.
    else:
        helloWorld_list = helloWorld.objects.all()
        return render(request, "accountapp/helloworld.html", context={"helloWorld_list": helloWorld_list})

class AccountCreateView(CreateView):
    model = User  # 장고 기본 제공 모델
    form_class = UserCreationForm  # 장고 기본 제공 폼
    success_url = reverse_lazy('accountapp:helloworld')  # reverse 함수형 reverse_lazy 클래스형
    template_name = 'accountapp/create.html'


class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    # 유저 별로 다르게 보이도록
    template_name = 'accountapp/detail.html'

@method_decorator(has_ownership, 'get') #접근 시 권한 필요
@method_decorator(has_ownership, 'post') #수정&삭제 시 권한 필요
class AccountUpdateView(PasswordChangeView):
    model = User
    form_class = PasswordChangeForm  # 장고 기본 제공 폼 / 강의와 다름
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:helloworld')  # reverse 함수형 reverse_lazy 클래스형
    template_name = 'accountapp/update.html'

    # detailview에 남아 있을 경우
    # def get_success_url(self):
    #     return reverse('accountapp:detail', kwargs={'pk': self.request.user.pk})

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:helloworld')  # reverse 함수형 reverse_lazy 클래스형
    template_name = 'accountapp/delete.html'
