import tweepy
import os

from social_bot.models.twitter_bot import TwitterBot
from social_bot.social_bot import SocialBot

if __name__ == '__main__':
    # ck = os.environ['consumer_key']
    # cs = os.environ['consumer_secret']
    # ak = os.environ['access_key']
    # ase = os.environ['access_secret']
    #
    # auth = tweepy.OAuthHandler(ck, cs)
    # auth.set_access_token(ak, ase)
    # api = tweepy.API(auth)
    # results = api.user_timeline(screen_name='elonmusk', count=1)
    # for r in results:
    #     print(r)

    bot = TwitterBot()
    ret = bot.fetch_posts()
    bot.upload_result(ret)
    print(str(ret))

