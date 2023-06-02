from django import forms
from .models import Post
from django.contrib.auth.models import Group
from allauth.account.forms import SignupForm


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content_header', 'content_text', 'category', 'author']


class CommonSignupForm(SignupForm):

    def save(self, request):
        user = super(CommonSignupForm, self).save(request)
        common_group = Group.objects.get(name='common')
        common_group.user_set.add(user)
        return user
