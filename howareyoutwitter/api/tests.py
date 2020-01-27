import json
import logging

from django.test import TestCase
from api.twitter_tools.response_handler import ResponseHandler


class ResponseHandlerTests(TestCase):
    
    def test_truncated(self):
        with open('test_response.json') as json_file:
            data = json.load(json_file)
            handler = ResponseHandler(data)
            tweets = handler.parse_tweets()
            self.assertTrue(len(tweets) > 1)

