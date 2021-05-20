import os
from typing import List

import tweepy

from social_bot.search_request import SearchRequest
from social_bot.search_results import SearchResult
from social_bot.social_bot import SocialBot


class TwitterBot(SocialBot):
    def __init__(self):
        super().__init__("twitter")

    def __fetch__(self, request: SearchRequest) -> List[SearchResult]:
        ck = os.environ['consumer_key']
        cs = os.environ['consumer_secret']
        ak = os.environ['access_key']
        ase = os.environ['access_secret']
        auth = tweepy.OAuthHandler(ck, cs)
        auth.set_access_token(ak, ase)
        api = tweepy.API(auth)
        results = api.user_timeline(screen_name=request.keyword, count=10)
        ret = []
        for r in results:
            obj = SearchResult(username=request.keyword, text=r.text, time=r.created_at, popularity=r.favorite_count,
                               post_id=r.id)
            in_reply_to = r.in_reply_to_status_id_str
            in_reply_to_name = r.in_reply_to_screen_name
            if in_reply_to:
                original_tweet = api.get_status(in_reply_to)
                original_tweet_obj = SearchResult(username=in_reply_to_name, text=original_tweet.text,
                                                  time=original_tweet.created_at,
                                                  popularity=original_tweet.favorite_count,
                                                  post_id=original_tweet.id,
                                                  related_to=r.id)
                ret.append(original_tweet_obj)
                obj.related_to = original_tweet_obj.post_id

            ret.append(obj)

        return ret
