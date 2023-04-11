from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View

from .models import Tweet, HashTag
from user_profile.models import User
from tweets.forms import TweetForm


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
        userProfile = User.objects.get(username=username)

        form = TweetForm(initial={'country': 'Global'})

        params["profile"] = userProfile
        params["form"] = form

        return render(request, 'profile.html', params)


class PostTweet(View):
    """Tweet Post form available on page /user/<username> URL"""

    def post(self, request, username):
        form = TweetForm(self.request.POST)
        if form.is_valid():
            user = User.objects.get(username=username)
            tweet = Tweet(text=form.cleaned_data['text'],
                          user=user,
                          country=form.cleaned_data['country'])
            tweet.save()
            words = form.cleaned_data['text'].split(" ")
            for word in words:
                if word[0] == "#":
                    hashtag, created = HashTag.objects.get_or_create(name=word[1:])
                    hashtag.tweet.add(tweet)
        return HttpResponseRedirect('/user/' + username)


class HashTagCloud(View):
    """Hash Tag page reachable from /hastag/<hashtag> URL"""

    def get(self, request, hashtag):
        params = dict()
        hashtag = HashTag.objects.get(name=hashtag)
        params["tweets"] = hashtag.tweet
        return render(request, 'hashtag.html', params)
