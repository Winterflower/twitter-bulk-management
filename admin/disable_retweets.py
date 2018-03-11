"""
Script to disable all retweets from people you follow
"""

import argparse
import requests
from requests_oauthlib import OAuth1
import os

API_ENDPOINT = 'https://api.twitter.com/1.1/friendships/update.json'

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('screen_name')
    return parser.parse_args()

def disable_retweets(screen_name, oauth):
    """
    Disables retweets from a single user
    """
    data = {'screen_name': screen_name, 
            'retweets': False }
    resp = requests.post(API_ENDPOINT, data=data, auth=oauth)
    return resp


def main():
    args = parse_args()
    oauth = OAuth1(os.environ['TWITTER_CONSUMER_KEY'], 
                   os.environ['TWITTER_CONSUMER_SECRET'],
                   os.environ['TWITTER_ACCESS_TOKEN'],
                   os.environ['TWITTER_ACCESS_SECRET'])
    resp = disable_retweets(args.screen_name, oauth)
    print(resp.text) 


if __name__ == '__main__':
    main()
