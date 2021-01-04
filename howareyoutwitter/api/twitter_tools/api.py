import requests
import json
import os
import twitter
from datetime import date, timedelta, datetime, time
from api import models
import dateutil.tz


# FIXME: No comments or automated tests here.
# FIXME: This name is not meaningful
class Api:
    def __init__(self, token=None):
        # Just go get the token if its None
        if token is None:
            credentials = twitter.Api().GetAppOnlyAuthToken(os.environ['CONSUMER_KEY'], os.environ['CONSUMER_SECRET'])
            token = models.Token(token_type=credentials['token_type'], access_token=credentials['access_token'])
            token.save()
        self.session = self.get_session(token)

    def get_session(self, token):
        session = requests.Session()
        session.trust_env = False
        headers = {'Accept-encoding': 'gzip'}
        headers['Authorization'] = f'Bearer {token.access_token}'
        session.headers = headers
        return session

    def post(self, url, data):
        response = self.session.post(url, data).json()
        return response

    def search(self, data):
        label = 'dev'
        url = f'https://api.twitter.com/1.1/tweets/search/30day/{label}.json'
        data = json.dumps(data)
        return self.post(url, data)

    def get_yesterday_to_and_from(self):
        yesterday = date.today() - timedelta(1)
        today = date.today()
        return yesterday, today

    def convert_date_to_data(self, datetime_obj: datetime):
        string_date = datetime.strftime(datetime_obj, '%Y%m%d%H%M')
        return string_date

    def date_search(self, hashtag: str, from_date: str, to_date: str, next_token=None):
        data = {'query': hashtag, 'fromDate': from_date, 'toDate': to_date, 'maxResults': 100}
        if next_token is not None:
            data['next'] = next_token
        response = self.search(data)
        return response

    def get_date_time(self, hour: int):
        # TODO: this tz should be configurable instead of hardcoded.
        date_time = datetime.now(dateutil.tz.gettz('America/Vancouver'))
        if hour < 24:
            date_time = date_time - timedelta(1)
        return date_time.replace(hour=hour, minute=0, second=0, microsecond=0).astimezone(dateutil.tz.tzutc())

    def daily_search(self, hashtag):
        hour_to_response = {}
        for start_hour in range(0, 24, 3):
            end_hour = start_hour + 3
            start_hour = start_hour

            start_time = self.convert_date_to_data(self.get_date_time(start_hour))
            end_time = self.convert_date_to_data(self.get_date_time(end_hour))

            response = self.date_search(hashtag, start_time, end_time)
            hour_to_response[start_hour] = response
        return hour_to_response
