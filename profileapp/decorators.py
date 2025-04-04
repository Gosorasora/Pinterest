from django.http import HttpResponseForbidden
from profileapp.models import Profile

def profile_ownership_required(func):
    def decorated(request, *args, **kwargs):
        #유저가 접근 할 때마다 그 유저의 pk를 확인함.
        profile = Profile.objects.get(pk=kwargs['pk'])

        #해당 유저가 아닐 경우엔 접근 제한
        if not profile.user == request.user:
            return HttpResponseForbidden()
        # 맞다면 리퀘스트 보냄
        return func(request, *args, **kwargs)
    return decorated