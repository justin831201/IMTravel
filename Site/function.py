from pymongo import MongoClient
from Site.models import Site

client = MongoClient(port=27017)
mongoDB = client["imtravel"]

scoreStandard = 2.3
minus = 1.7
multiple = 1.8

def keywordOfSites(sites, num):
    keywordCollection = mongoDB["台北keyword"]
    keywords = list(keywordCollection.find({}))
    result = []
    for site in sites:
        for keyword in keywords:
            if keyword['site'] == site.name:
                site.keywords = keyword['keywords'][:num]
                result.append(site)
                break
    return result

def scoreOfSites(sites):
    scoreCollection = mongoDB["台北score"]
    keywordCollection = mongoDB["台北keyword"]
    scores = list(scoreCollection.find({}))
    keywords = list(keywordCollection.find({}))
    result = []
    for site in sites:
        for score in scores:
            if score['site'] == site.name:
                site.classmateAsset = score['classmateTimes']
                site.coupleAsset = score['coupleTimes']
                site.childrenAsset = score['childTimes']
                site.familyAsset = score['familyTimes']
                site.boyAsset = score['boyTimes']
                site.girlAsset = score['girlTimes']
                site.score = scoreModifiedValue(typeOfScore="score", scoreTable=score)
                site.classmateScore = scoreModifiedValue(typeOfScore="classmateScore", scoreTable=score)
                site.coupleScore = scoreModifiedValue(typeOfScore="coupleScore", scoreTable=score)
                site.childrenScore = scoreModifiedValue(typeOfScore="childScore", scoreTable=score)
                site.familyScore = scoreModifiedValue(typeOfScore="familyScore", scoreTable=score)
                site.boyScore = scoreModifiedValue(typeOfScore="boyScore", scoreTable=score)
                site.girlScore = scoreModifiedValue(typeOfScore="girlScore", scoreTable=score)
                result.append(site)
                break
    return result

def productOfSite(site):
    temp = list(site)
    scoreCollection = mongoDB['台北score']
    scores = list(scoreCollection.find({}))
    for score in scores:
        if score['site'] == temp[0].name:
            temp[0].productNumber = score['product']['product_num']
            temp[0].productPrice = score['product']['price']
            temp[0].productName = score['product']['name']
            temp[0].productEachNumber = score['product']['price_num']
            temp[0].time = score['times']
            break
    return temp

def scoreModifiedValue(typeOfScore, scoreTable):
    modifiedValue = 1
    if scoreTable[typeOfScore] >= scoreStandard:
        modifiedValue = round((scoreTable[typeOfScore]-minus)*multiple)
        if modifiedValue > 5:
            modifiedValue = 5
    return modifiedValue

