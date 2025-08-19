from django.forms.models import ModelForm
from pkg_resources import require

from articleapp.models import Article
from django import forms

from projectapp.models import Project


class ArticleCreationForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'editalble text=left',
                                                           'style':'height:auto;'}))
    project = forms.ModelChoiceField(queryset = Project.objects.all(), required=False)

    class Meta:
        model = Article
        fields = ['title', 'image', 'project', 'content']