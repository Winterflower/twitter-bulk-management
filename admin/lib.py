"""
Library for shared code
"""

import tweepy
import os


def get_auth():
    consumer_key = os.environ['TWITTER_CONSUMER_KEY']
    consumer_secret = os.environ['TWITTER_CONSUMER_SECRET']
    access_token = os.environ['TWITTER_ACCESS_TOKEN']
    access_token_secret = os.environ['TWITTER_ACCESS_SECRET']
    auth = tweepy.OAuthHandler(consumer_key,
            consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return auth


def create_api():
    api = tweepy.API(get_auth())
    return api

def get_friends(screen_name, api):
    friends = api.friends_ids(screen_name)
    print(len(friends))
    return friends
