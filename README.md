# DigitalHumanProject

## Summary
This project is related to the course "Subjects in Digital humanities".
In this project I hoped to achive a

#

## Related sources
### API - News Api
**https://newsapi.org/**
### Yap - Yet Another (natural language) Parser
**https://github.com/OnlpLab/yap**
### Artice - A Unified Morpho-Syntactic Scheme of Stanford Dependencies
**http://www.tsarfaty.com/pdfs/acl13.pdf**

#
# The Process

## Set up and activate

### <b><u>Prerequirements</u></b>
* python3
* go
* create apikey for [NewsAPI](https://newsapi.org/)
* install and compile [YAP](https://github.com/OnlpLab/yap) - make sure you do it inside `GOPATH`

### <b><u>activate venv</u></b>
```
cd <your project dir>
git clone <git url>
cd DigitalHumanProject
```
### <b><u>activate venv</u></b>
```
python3.7 -m venv venv3
source venv3/bin/activate
```
### <b><u>install project requirements</u></b>

```
pip3 install -r requirements.txt
export api_key=<YOUR_API_KEY>
```
(example: export api_key=40d61a5ed053486f8b3ef093551f4d40)

### <b><u>deactivate venv (if needed)</u></b>
```
deactivate
```
# 

## Action & Explaination

Our target is to extract 

<u>For that, We'll apply 4 steps:</u>

### Phase #1 (manually)
Prepare you research:

In these project I focused on Israelies politicians, <br>
but it can be applied to any context you wish to research. 

### Phase #2 (manually)
Get contenct into jsons with the following structure:
```
{"status": "ok", 
"totalResults": 16, 
"articles": [
    {"source": {"id": "ynet", "name": "Ynet"},
    "author": "...", 
    "description": "...", 
    "url": "'''", 
    "publishedAt": "2020-01-01T20:00:00Z", "content": "..."},
    ...
]
}
```
* The files will be saved in content/json/name/
* In our project the files contains articles with politicians names, but it can be applied to any name you want

### Phase #3 (automatically)
Extracting tokens from the content.

Assuming the content is set in the right way,</br>
this phase will extract the content and parse it into tokens.

An example for a token file:

```
חבר
הכנסת
מהליכוד
טען
באולפן
ynet
כי
למרות
שראש
הממשלה
נתניהו
יישב
על
ספסל
הנאשמים,
"הניסיון
שלו
כל
כך
משמעותי,
שאדם
עם
אפס
צרות
אחרות
לא
מסוגל
להיכנס
לנעליו".
הוא
גיבה
את
בנט
למרות
המתקפות
נגדו:
"שר
ביטחון
טוב".
על
גדעון
סער:
"נתניהו
מבין
היטב
את
מקומו
בהנהג…
 
.

```
* The files will be saved in tokens/name/

### Phase #4 (automatically)
Applying YAP utils on our tokens

In this step, we'll apply yap utils to extract "Part of speech" in Hebrew.

* The files will be saved in finalresults/name/

#
 
# Project specifications

## Work with `Makefile`

```
make api-data
```
``` 
make extract-tokens
```
```
make apply-yap
```
```
make delete-results
```
```
make restart
```
```	
make start
```

### examples for api call

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