from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import View

from .models import Tweet
from user_profile.models import User


class Index(View):

    def get(self, request):
        params = {}
        params["name"] = "Django_learn_YJ"
        return render(request, 'base.html', params)


def post(self, request):
    return HttpResponse('I am called from a post Request')


class Profile(View):
    """User Profile page reachable from /user/<username> URL"""

    def get(self, request, username):
        params = dict()
        user = User.objects.get(username=username)
        tweets = Tweet.objects.filter(user=user)
        params["tweets"] = tweets
        params["user"] = user
        return render(request, 'profile.html', params)
