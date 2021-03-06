from newsapi import NewsApiClient
import json
import os

politicians = {"bibi": ['בינימין נתניהו','ביבי','נתניהו','בינימין נתניהו','ראש הממשלה','בנימין נתניהו'],
               "gantz": ['בני גנץ','גנץ','בני גנץ','בנימין גנץ','בינימין גנץ'],
               "liberman": ['אביגדור ליברמן','אביגדור איווט ליברמן','ליברמן'],
               "gabi": ['גבי אשכנזי'],
               "lapid": ['יאיר לפיד'],
               "amir": ['עמיר פרץ'],
               "stav": ['סתיו שפיר'],
               "gidon": ['גדעון סער'],
               "miri": ['מירי רגב'],
               "shaked": ['איילת שקד'],
               "benet": ['נפתלי בנט'],
               "tibi": ['טיבי', 'אחמד טיבי'],
               "rafi": ['רפי פרץ'],}

api_key = os.environ.get('api_key')

newsapi = NewsApiClient(api_key=api_key)

for p in politicians:
    i = 0
    for p1 in politicians[p]:
        os.makedirs(os.path.dirname('content/json/{p}/{i}newsdata.json'.format(p=p, i=i)), exist_ok=True)
        os.makedirs(os.path.dirname('content/text/{p}/{i}newsdata.txt'.format(p=p, i=i)), exist_ok=True)
        with open('content/json/{p}/{i}newsdata.json'.format(p=p, i=i), 'a+', encoding='utf-8') as f:
            with open('content/text/{p}/{i}newsdata.txt'.format(p=p, i=i), 'a+', encoding='utf-8') as t:
                print(p1)
                all_articles = newsapi.get_everything(q=p1)
                json.dump(all_articles, f)
                print(all_articles, file=t)
                i = i + 1

# print(json.dumps(all_articles))