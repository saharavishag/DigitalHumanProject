import json
import os

politicians = {'bibi', 'gantz', 'liberman', 'gabi', 'lapid', 'amir', 'stav',
               'gidon', 'miri', 'shaked', 'benet', 'tibi', 'rafi'}

def get_num_of_files(directory):
    # directory = 'content/json/bibi'
    number_of_files = len([item for item in os.listdir(directory) if os.path.isfile(os.path.join(directory, item))])
    return number_of_files

for p in politicians:
    k = get_num_of_files('content/json/{}'.format(p))
    # print(k)
    for j in range(k):
        try:
            with open('content/json/{}/{}newsdata.json'.format(p, j), 'r+', encoding="utf-8") as f:
                data = json.load(f)
                print(data)
                sentence = 0
                for article in data['articles']:
                    os.makedirs(
                        os.path.dirname('tokens/{}/{}tokens.txt'.format(p, j)), exist_ok=True)
                    with open('tokens/{}/{}.{}tokens.txt'.format(p, j, sentence), 'a+', encoding='utf-8') as t:
                        # prepare file for yap
                        c = '\n'.join((article['description']).split(" ") + [' ', '.'])
                        print(c, file=t)
                        print(c)
                    sentence = sentence + 1
        except Exception as e:
            print('error occurred with {}'.format(p))
            print(e)
