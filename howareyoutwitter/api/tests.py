import json
import logging

from django.test import TestCase
from api.twitter_tools.response_handler import ResponseHandler
from api.twitter_tools.api import Api as TwitterApi
from api.models import Token


class TestResponseHandler(TestCase):

    # TODO: Break this into unit tests rather than one big integration test
    def test_parse_tweets(self):
        with open('test_response.json') as json_file:
            data = json.load(json_file)
            handler = ResponseHandler(data)
            tweets = handler.parse_tweets()
            self.assertTrue(len(tweets) > 1)

class TestApi(TestCase):

    def setUp(self):
        self.fake_token = Token.objects.create(token_type="fake_type", access_token="fake_token")

    # TODO: test the date stuff
