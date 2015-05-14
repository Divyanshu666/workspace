from TwitterAPI import *

import tweepy
import re

from random import *
CONSUMER_KEY = 'bhipusATdYgFpi9W2nCaHK57c'
CONSUMER_SECRET = 'XwTylNDMSogXIMhKEwc5uaSPTcyYkTDbfHj6ZifWxZu3oLl0RJ'

ACCESS_TOKEN = '994668080-T9nQ2EH6LBZFeND2HKJ0mfcj0Zm5lUZ57uSNQ0Hx'
ACCESS_SECRET = '72ppPOwj3vZtetdZXTLm8YSv3ZCCId0w1rEIQloBR8VQx'

GEOCODE = '28.5703170,77.3218200'

TWITTER_API  = 'https://api.twitter.com/1.1/trends/place.json?id=1'

hashtags = 'DhoniRetires'
query = "#"+hashtags


twitter = TwitterAPI(consumer_key= CONSUMER_KEY,consumer_secret= CONSUMER_SECRET,access_token_key=ACCESS_TOKEN,access_token_secret=ACCESS_SECRET)

r = twitter.request('trends/place',{'q':'Trending', 'geocode':'28.5703170,77.3218200,200km','count':'10'})

for item in r.get_iterator():
	tweet = {}
	# print item['name']
	print item
	print item['user']['screen_name'] + " said : \n" + item['text']
	re.findall(r"#(\w+)", item['text'])


# trends1 = api.trends_place(1)
# print trends1
# hashtags = [x['name'] for x in trnd[0]['trends'] if x['name'].startswith('#')]
# # print hashtags
# print hashtags[0]
# trend_hashtag = hashtags[0]
# api.update_status("{0} {1}".format(line, trend_hashtag)) # more modern format
# time.sleep(1800)


trends = api.GetTrendsCurrent()
for trend in trends:
	print trend.name

auth = tweepy.OAuthHandler(consumer_key=CONSUMER_KEY,consumer_secret=CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_SECRET)

api = tweepy.API(auth)
trends1 = api.trends_place(1)

hashtags = [x['name'] for x in trends1[0]['trends']]

for tags in hashtags:
	ripped = re.sub("#","",tags)