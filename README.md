# DigitalHumanProject

### activate venv

python3.7 -m venv venv3
source venv3/bin/activate
pip3 install -r requirements.txt
<br>
`export api_key=40d61a5ed053486f8b3ef093551f4d40`

### deactivate venv

deactivate

### examples

```
newsapi = NewsApiClient(api_key='40d61a5ed053486f8b3ef093551f4d40')

top_headlines = newsapi.get_top_headlines(q='bitcoin',
                                          sources='bbc-news,the-verge',
                                          category='business',
                                          language='en',
                                          country='us')

all_articles = newsapi.get_everything(q='bitcoin',
                                      sources='bbc-news,the-verge',
                                      domains='bbc.co.uk,techcrunch.com',
                                      from_param='2017-12-01',
                                      to='2017-12-12',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)
```
### Result structure from the API
Json

Each item:

{
    "source": {"id": "ynet", "name": "Ynet"}, 
    "author": "...", 
    "description": "..."", 
    "url": "...", 
    "urlToImage": "...", 
    "publishedAt": 
    "2020-01-25T16:51:00Z", 
    "content": "..."
}