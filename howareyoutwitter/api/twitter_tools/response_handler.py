import logging

from datetime import datetime
from api.models import Tweet, Hashtag

class ResponseHandler():
    def __init__(self, response):
        try:
            self.tweets = response['results']
        except KeyError:
            raise KeyError(f'Tried to get results but response looks like:\n{response}')
        try:
            self.next = response['next']
        except KeyError:
            self.next = 'null'

    # TODO: The create_tweet and create_hastag functions are going to be very
    # slow due to it creating a DB transaction for every tweet. We can make use
    # of Django's bulk_create functions to speed it up.
    def parse_tweets(self):
        tweet_models = []
        for tweet in self.tweets:
            user_id = tweet['user']['id_str']
            tweet_id = tweet['id_str']
            creation_date = self.get_date_time(tweet['created_at'])
            text = self.get_text(tweet)

            hashtags = tweet['entities']['hashtags']
            hashtags = self.create_hashtag_models(hashtags)

            tweet_model, created = self.create_tweet_model(user_id, tweet_id, creation_date, text, hashtags)
            tweet_models.append(tweet_model)

        return tweet_models

    def create_hashtag_models(self, hashtags: dict):
        model_list = []
        for hashtag in hashtags:
            hashtag, created = Hashtag.objects.get_or_create(text=hashtag['text'])
            model_list.append(hashtag)
        return model_list

    def create_tweet_model(self, user_id, tweet_id, creation_date, text, hashtags):
        tweet, created = Tweet.objects.get_or_create(user_id=user_id, tweet_id=tweet_id, creation_date=creation_date, text=text)
        for hashtag in hashtags:
            tweet.hashtags.add(hashtag)
        return tweet, created

    def get_date_time(self, date_time_string):
        #"created_at": "Sat Jan 11 23:58:32 +0000 2020"
        format = "%a %b %d %H:%M:%S %z %Y"
        date_time = datetime.strptime(date_time_string, format)
        return date_time

    def get_text(self, tweet: dict):
        # TODO: KeyError?
        if 'truncated' in tweet:
            truncated = tweet['truncated']
            if truncated:
                text = tweet['extended_tweet']['full_text']
                return text
        text = tweet['text']
        return text
