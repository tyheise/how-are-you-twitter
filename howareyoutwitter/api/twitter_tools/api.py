import requests
import json
from datetime import date, timedelta, datetime


class Api:
    def __init__(self, token):
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
        return self.convert_date_to_data(yesterday), self.convert_date_to_data(today)

    def convert_date_to_data(self, date):
        string_date = datetime.strftime(date, '%Y%m%d')
        return f"{string_date}0000"

    def daily_search(self, hashtag):
        fromDate, toDate = self.get_yesterday_to_and_from()
        data = {'query': hashtag, 'fromDate': fromDate, 'toDate': toDate}
        response = self.search(data)
        return response

    def date_search(self, hashtag, fromDate, toDate):
        fromDate = self.convert_date_to_data(fromDate)
        toDate = self.convert_date_to_data(toDate)
        data = {'query': hashtag, 'fromDate': fromDate, 'toDate': toDate}
        response = self.search(data)
