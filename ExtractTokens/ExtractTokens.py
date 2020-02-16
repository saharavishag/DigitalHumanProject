import json
import os

politicians = {'bibi', 'gantz', 'liberman', 'gabi', 'lapid', 'amir', 'stav',
               'gidon', 'miri', 'shaked', 'benet', 'tibi', 'rafi'}

for p in politicians:
    print(p)
    try:
        with open('content/json/{p}/newsdata.json'.format(p=p), 'r+', encoding="utf-8") as f:
            i = 0
            for item in f:
                data = json.loads(item)
                for article in data['articles']:
                    os.makedirs(
                        os.path.dirname('tokens/{p}/{i}tokens.txt'.format(p=p, i=i)), exist_ok=True)
                    with open('tokens/{p}/{i}tokens.txt'.format(p=p, i=i), 'a+', encoding='utf-8') as t:
                        print((article['description']).split(" ") + [' ', '.'], file=t)
                        print((article['description']).split(" ") + [' ', '.'])
                    i = i + 1
    except Exception as e:
        print('error occurred with {}'.format(p))
        print(e)
