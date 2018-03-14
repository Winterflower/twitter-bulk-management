"""
Script for bulk unfollowing
"""
import tweepy
import os
import argparse

from lib import get_auth, create_api, get_friends

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('twitterhandle')
    return parser.parse_args()


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
