# News API: f3708f733de54a68acef9f7305fd9702
import requests


class NewsFeed:
    """Representing multiple news titles and links as a single string"""
    base_url = "http://newsapi.org/v2/everything?"
    api_key = "f3708f733de54a68acef9f7305fd9702"

    def __init__(self, interest, from_date, end_date, language):
        self.interest = interest
        self.from_date = from_date
        self.end_date = end_date
        self.language = language

    def _build_url(self):
        url = f"{self.base_url}" \
              f"q=Apple" \
              f"&from={self.from_date}" \
              f"&to={self.end_date}" \
              f"&language={self.language}" \
              f"&apiKey={self.api_key}"
        return url

    def _get_articles(self, url):
        response = requests.get(url)
        content = response.json()
        articles = content['articles']
        return articles

    def get(self):
        url = self._build_url()
        articles = self._get_articles(url)
        articles_body = ""
        for article in articles:
            articles_body = articles_body + article['title'] + "\n" + article['url'] + "\n\n"

        return articles_body


if __name__ == "__main__":
    news_feed = NewsFeed("Apple", "2022-08-15", "2022-08-15", "en")
    articles = news_feed.get()
    print('articles : ', articles)
