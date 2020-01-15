from newsapi import NewsApiClient
import json
import os

api_key = os.environ.get('api_key')

newsapi = NewsApiClient(api_key=api_key)

all_articles = newsapi.get_everything(q='ביבי')

print(all_articles)
# print(json.dumps(all_articles))