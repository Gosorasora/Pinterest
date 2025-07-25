from django.http import HttpResponseForbidden
from articleapp.models import Article

def article_ownership_required(func):
    def decorated(request, *args, **kwargs):
        article = Article.objects.get(pk=kwargs['pk'])
        #해당 writer가 아닐 경우엔 접근 제한
        if not article.writer == request.user:
            return HttpResponseForbidden()
        # 맞다면 리퀘스트 보냄
        return func(request, *args, **kwargs)
    return decorated