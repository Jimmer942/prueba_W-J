#!/usr/bin/env python3

from aylienapiclient import textapi

client = textapi.Client("997164d6", "ea4a6cb4b1fffbc1739ae8995ca50a37")

def get_news_info(url):
    data = dict()
    print(url)
    print('------------classifications--------------------')
    classifications = client.Classify({"url": url})
    text = classifications['text']
    data['classification'] = classifications['categories'][0]
    
    print('------------sentiment--------------------')
    sentiment = client.Sentiment({'text': text})
    del sentiment['text']
    data['sentiment'] = sentiment
    
    print('-----------Elsa---------------------')
    elsa = client.Elsa({'text': text})
    data['elsa'] = elsa['entities']


    print('------------entities--------------------')
    entities = client.Entities({"text": text})
    data['entities'] = entities['entities']


    print('----------concepts----------------------')
    concepts = client.Concepts({"text": text})
    data['concepts'] = concepts['concepts']
        
    print('-------------summary-------------------')
    summary = client.Summarize({'url': url, 'sentences_number': 3})
    data['summary'] = summary['sentences']
    print('------------------------------------------')
    return data
