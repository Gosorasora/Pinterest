from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from profileapp.decoratros import profile_ownership_required
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


# Create your views here.

class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountapp:helloworld')
    template_name = 'profileapp/create.html'

    def form_valid(self, form):
        try:
            # 현재 사용자에게 이미 프로필이 있는지 확인
            existing_profile = Profile.objects.get(user=self.request.user)
            return self.form_invalid(form)  # 이미 있으면 폼을 유효하지 않게 처리
        except ObjectDoesNotExist:
            # 프로필이 없으면 새로 생성
            temp_profile = form.save(commit=False)
            temp_profile.user = self.request.user
            temp_profile.save()
            return super().form_valid(form)

@method_decorator(profile_ownership_required(), 'get')
@method_decorator(profile_ownership_required(), 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountapp:helloworld')
    template_name = 'profileapp/update.html'
