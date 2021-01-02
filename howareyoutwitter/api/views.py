import requests
import twitter
import os
import logging
import json

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Token
from api.twitter_tools import api as twitter_tools_api
from api.twitter_tools.tweet_seeker import TweetSeeker

# TODO: These views don't really make sense. The logic these handle should be
# in some background process.

class AuthenticateView(APIView):

    def get(self, request):
        credentials = twitter.Api().GetAppOnlyAuthToken(os.environ['CONSUMER_KEY'], os.environ['CONSUMER_SECRET'])
        token = Token(token_type=credentials['token_type'], access_token=credentials['access_token'])
        token.save()
        return Response(credentials)

# 25000 tweets a month. 800 tweets a day. 33 tweets an hour.
# 250 requests a month. 8 requests a day. 0.33 requests an hour.
class SearchTweetsView(APIView):

    def get(self, request):
        """
        query = {'geocode': '53.631611, -113.323975, 12.5km', ''}
        """
        tokens = Token.objects.all()
        token = None
        try:
            token = tokens[0]
        except IndexError:
            raise IndexError('No Authentication token')

        t_s = TweetSeeker(token)
        t_s.run('#yeg')

        return Response('success!')
