import datetime


class SearchResult:
    def __init__(self, post_id: str, username: str, text: str, time: str, popularity: int, related_to: str = None):
        self.username = username
        self.text = text
        self.datetime = time
        self.popularity = popularity
        self.post_id = post_id
        self.related_to = related_to

    def to_json(self):
        return {"username": self.username, "text": self.text, "time": str(self.datetime),
                "popularity": self.popularity, "post_id": self.post_id, "related_to": self.related_to}
