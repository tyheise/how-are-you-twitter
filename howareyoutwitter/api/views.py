import requests
import twitter
import os

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class AuthenticateView(APIView):

    def get(self, request):
        credentials = twitter.Api().GetAppOnlyAuthToken(os.environ['CONSUMER_KEY'], os.environ['CONSUMER_SECRET'])
        return Response(credentials)

        
