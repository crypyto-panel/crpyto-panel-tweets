class SearchRequest:
    def __init__(self, keyword: str):
        """
        Construct a search request object. Twitter will use as username,
        and weibo will use as keyword
        :param keyword:
        """
        self.keyword = keyword

    @staticmethod
    def from_json(json):
        return SearchRequest(keyword=json['keyword'])

    def __str__(self):
        return f"<SearchRequest: {self.keyword} />"
