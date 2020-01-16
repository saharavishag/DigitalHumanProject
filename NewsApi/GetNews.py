from newsapi import NewsApiClient
import json
import os

politicians = [['בינימין נתניהו','ביבי','נתניהו','בינימין נתניהו','ראש הממשלה','בנימין נתניהו'],
               ['בני גנץ','גנץ','בני גנץ','בנימין גנץ','בינימין גנץ'],
               ['אביגדור ליברמן','אביגדור איווט ליברמן','ליברמן'],
               ['גבי אשכנזי'],
               ['יאיר לפיד'],
               ['עמיר פרץ'],
               ['סתיו שפיר'],
               ['גדעון סער'],
               ['מירי רגב'],
               ['איילת שקד'],
               ['נפתלי בנט'],
               ['טיבי'],
               ['רפי פרץ'],]

api_key = os.environ.get('api_key')

newsapi = NewsApiClient(api_key=api_key)

all_articles = newsapi.get_everything(q='ביבי')

print(all_articles)
# print(json.dumps(all_articles))