from newsapi import NewsApiClient
import json
import os

politicians = [['בינימין נתניהו','ביבי','נתניהו','בינימין נתניהו','ראש הממשלה','בנימין נתניהו'],
               ['בני גנץ','גנץ','בני גנץ','בנימין גנץ','בינימין גנץ'],
               ['אביגדור ליברמן','אביגדור איווט ליברמן','ליברמן'],
               [],
               [],
               [],
               [],]

api_key = os.environ.get('api_key')

newsapi = NewsApiClient(api_key=api_key)

all_articles = newsapi.get_everything(q='ביבי')

print(all_articles)
# print(json.dumps(all_articles))