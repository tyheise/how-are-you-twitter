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

class AuthenticateView(APIView):

    def get(self, request):
        credentials = twitter.Api().GetAppOnlyAuthToken(os.environ['CONSUMER_KEY'], os.environ['CONSUMER_SECRET'])
        token = Token(token_type=credentials['token_type'], access_token=credentials['access_token'])
        token.save()
        return Response(credentials)

        
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

        api = twitter_tools_api.Api(token)
        response = api.daily_search('#yeg')


        tweets = response['results']
        for tweet in tweets:
            user_id = tweet['user']['id']
            truncated = tweet['truncated']

            

        return Response(response)

