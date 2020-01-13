from django.db import models

# Create your models here.
class Token(models.Model):
    token_type = models.CharField(max_length=300)
    access_token = models.CharField(max_length=300)

class Tweet(models.Model):
    user_id = models.CharField(max_length=300)
    tweet_id = models.CharField(max_length=300)
    creation_date = models.DateTimeField()
    text = models.CharField(max_length=300)

class Hashtag(models.Model):
    text = models.CharField(max_length=300, unique=True)

class TweetHashtag(models.Model):
    tweet = models.ForeignKey('Tweet', on_delete=models.CASCADE)
    hashtag = models.ForeignKey('Hashtag', on_delete=models.CASCADE)