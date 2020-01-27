import logging

from django.core.management.base import BaseCommand
from api import models


class Command(BaseCommand):
    help = 'delete models'

    def handle(self, *args, **options):
        tweets = models.Tweet.objects.all()
        for tweet in tweets:
            tweet.delete()

        hashtags = models.Hashtag.objects.all()
        for hashtag in hashtags:
            hashtag.delete()

        logging.info('Succesfully deleted all tweets and hashtags')