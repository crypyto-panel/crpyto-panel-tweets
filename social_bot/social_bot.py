import os
from typing import List
from supabase_py import create_client, Client
from social_bot.search_request import SearchRequest
from social_bot.search_results import SearchResult


class SocialBot:
    def __init__(self, target_type: str):
        self.target_type = target_type
        self.url = os.environ.get('supabase_url')
        self.key = os.environ.get('supabase_key')

    def fetch_requests(self) -> List[SearchRequest]:
        supabase: Client = create_client(self.url, self.key)
        data = supabase.table('search_request').select(f"*").filter('datasource', 'eq', self.target_type).execute()
        data = data.get('data')
        ret = [SearchRequest.from_json(d) for d in data]
        return ret

    def fetch_posts(self):
        reqs = self.fetch_requests()
        res_l = []
        for req in reqs:
            res = self.__fetch__(req)
            res_l += res

        return res_l

    def upload_result(self, search_results: List[SearchResult]):
        supabase: Client = create_client(self.url, self.key)
        for r in search_results:
            data = supabase.table("posts").insert(r.to_json()).execute()
            print(data)
            assert len(data.get("data", [])) > 0

    def __fetch__(self, request: SearchRequest) -> List[SearchResult]:
        raise NotImplementedError
