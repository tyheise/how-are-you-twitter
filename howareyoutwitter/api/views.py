import requests
import twitter
import os

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Token

class AuthenticateView(APIView):

    def get(self, request):
        credentials = twitter.Api().GetAppOnlyAuthToken(os.environ['CONSUMER_KEY'], os.environ['CONSUMER_SECRET'])
        token = Token(token_type=credentials['token_type'], access_token=credentials['access_token'])
        token.save()
        return Response(credentials)

        
