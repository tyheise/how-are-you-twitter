import logging

from datetime import datetime
from api.models import Tweet, Hashtag, TweetHashtag

class ResponseHandler():
    def __init__(self, response):
        self.tweets = response['results']
        self.next = response['next']

    def parse_tweets(self):
        tweet_models = []
        for tweet in self.tweets:
            user_id = tweet['user']['id_str']
            tweet_id = tweet['id_str']
            creation_date = self.get_date_time(tweet['created_at'])
            text = self.get_text(tweet)
            tweet_model, created = self.create_tweet_model(user_id, tweet_id, creation_date, text)
            tweet_models.append(tweet_model)

            hashtags = tweet['entities']['hashtags']
            hashtags = self.create_hashtag_models(hashtags, tweet_model)

        return tweet_models

    def create_hashtag_models(self, hashtags: dict, tweet: Tweet):
        model_list = []
        for hashtag in hashtags:
            hashtag, created = Hashtag.objects.get_or_create(text=hashtag['text'])
            TweetHashtag.objects.get_or_create(tweet=tweet, hashtag=hashtag)
            model_list.append(hashtag)
        return model_list

    def create_tweet_model(self, user_id, tweet_id, creation_date, text):
        tweet = Tweet.objects.get_or_create(user_id=user_id, tweet_id=tweet_id, creation_date=creation_date, text=text)
        return tweet

    def get_date_time(self, date_time_string):
        #"created_at": "Sat Jan 11 23:58:32 +0000 2020"
        format = "%a %b %d %H:%M:%S %z %Y"
        date_time = datetime.strptime(date_time_string, format)
        return date_time

    def get_text(self, tweet: dict):
        truncated = tweet['truncated']
        if truncated:
            text = tweet['extended_tweet']['full_text']
        else:
            text = tweet['text']
        return text

        