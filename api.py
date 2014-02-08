import json
import urllib3
import random


def parseWord(word):
    word=str(word)
    l=word.replace(" ","+")
    return l

def getResult(word):
    keyword=parseWord(word)
    api="http://socialmention.com/search?q="+keyword+"&f=json&t=microblogs&lang=fr"
    http=urllib3.PoolManager()
    request=http.request('GET',api)
    result=json.loads(request.data)
    return result

def getCount(keyword):
    result=getResult(keyword)
    return result['count']

def getSenAuth(keyword):
    result=getResult(keyword)
    rand=random.randint(0,len(result['items'])-2)
    sentence=result['items'][rand]['title']
    author=result['items'][rand]['user']
    origin=result['items'][rand]['source']
    return {'sentence':sentence,'author':author,'origin':origin}

print getSenAuth("I am cool")


    
