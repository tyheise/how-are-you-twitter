import logging

from api.twitter_tools.api import Api
from api.twitter_tools.response_handler import ResponseHandler

class TweetSeeker:
    def __init__(self, token):
        self.token = token

    def run(self, hashtag: str):
        """
        Main application logic for gathering tweets
        args: string like '#yeg'
        """
        api = Api(self.token)
        response = api.daily_search(hashtag)
        handler = ResponseHandler(response)
        handler.parse_tweets()
        nextToken = handler.next
        while nextToken != 'null':
            logging.error(f"next: {nextToken}")
            response = api.daily_search(hashtag, nextToken)
            handler = ResponseHandler(response)
            handler.parse_tweets()
            nextToken = handler.next
            
        return 0

