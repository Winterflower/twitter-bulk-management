"""
Script to disable all retweets from people you follow
"""

import argparse
import requests
from requests_oauthlib import OAuth1
import os

from lib import get_friends, create_api

API_ENDPOINT = 'https://api.twitter.com/1.1/friendships/update.json'

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('screen_name')
    return parser.parse_args()

def disable_retweets(userid, oauth):
    """
    Disables retweets from a single user
    """
    data = {'user_id': userid, 
            'retweets': False }
    resp = requests.post(API_ENDPOINT, data=data, auth=oauth)
    return resp


def main():
    args = parse_args()
    oauth = OAuth1(os.environ['TWITTER_CONSUMER_KEY'], 
                   os.environ['TWITTER_CONSUMER_SECRET'],
                   os.environ['TWITTER_ACCESS_TOKEN'],
                   os.environ['TWITTER_ACCESS_SECRET'])
    api = create_api()
    friends = get_friends(args.screen_name, api)
    for f_id in friends:
        resp = disable_retweets(f_id, oauth)
        


if __name__ == '__main__':
    main()
