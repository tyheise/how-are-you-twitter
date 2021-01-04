from api import models
from api.twitter_tools.tweet_seeker import TweetSeeker


def retrieve_tweets():
    tokens = models.Token.objects.all()
    try:
        token = tokens[0]
    except IndexError:
        token = None

    t_s = TweetSeeker(token)
    t_s.run('#vancouver')
