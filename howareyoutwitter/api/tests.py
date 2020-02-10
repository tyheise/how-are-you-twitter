import json
import logging

from django.test import TestCase
from api.twitter_tools.response_handler import ResponseHandler
from api.twitter_tools.api import Api as TwitterApi
from api.models import Token


class ResponseHandlerTests(TestCase):
    
    def test_truncated(self):
        with open('test_response.json') as json_file:
            data = json.load(json_file)
            handler = ResponseHandler(data)
            tweets = handler.parse_tweets()
            self.assertTrue(len(tweets) > 1)

class ApiTests(TestCase):

    def setUp(self):
        self.fake_token = Token.objects.create(token_type="fake_type", access_token="fake_token")

    def test_new_thing(self):
        api = TwitterApi(self.fake_token)
        api.new_thing()

