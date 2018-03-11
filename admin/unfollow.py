"""
Script for bulk unfollowing
"""
import tweepy
import os
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('twitterhandle')
    return parser.parse_args()

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

def unfollow(ids, api):
    for u_id in ids:
        api.destroy_friendship(u_id)

def main():
    args = parse_args()
    api = create_api()
    ids = get_friends(args.twitterhandle, api)
    if ids:
        unfollow(ids, api)
    else:
        print('Looks like your Twitter account does not follow any other accounts')


if __name__ == '__main__':
    main()
