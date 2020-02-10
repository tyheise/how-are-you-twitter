import logging

from api.twitter_tools.api import Api
from api.twitter_tools.response_handler import ResponseHandler


# 25000 tweets a month. 800 tweets a day. 33 tweets an hour.
# 250 requests a month. 8 requests a day. 0.33 requests an hour.
class TweetSeeker:
    def __init__(self, token):
        self.token = token

    def run(self, hashtag: str):
        """
        Main application logic for gathering tweets
        args: string like '#yeg'
        """
        api = Api(self.token)
        response_dict = api.daily_search(hashtag)
        for hour in response_dict:
            handler = ResponseHandler(response_dict[hour])
            handler.parse_tweets()

        return 0

