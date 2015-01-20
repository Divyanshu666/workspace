import json
import urllib
import requests
import django.utils.simplejson as json
import twitter
import googlemaps
import tweepy
import re

def twitter_trend_hashtag():

	CONSUMER_KEY = 'bhipusATdYgFpi9W2nCaHK57c'
	CONSUMER_SECRET = 'XwTylNDMSogXIMhKEwc5uaSPTcyYkTDbfHj6ZifWxZu3oLl0RJ'

	ACCESS_TOKEN = '994668080-T9nQ2EH6LBZFeND2HKJ0mfcj0Zm5lUZ57uSNQ0Hx'
	ACCESS_SECRET = '72ppPOwj3vZtetdZXTLm8YSv3ZCCId0w1rEIQloBR8VQx'

	# url = 'https://api.twitter.com/1.1/trends/place.json?id=1'
	twitter_api = twitter.Api(consumer_key=CONSUMER_KEY,consumer_secret=CONSUMER_SECRET,access_token_key=ACCESS_TOKEN,access_token_secret=ACCESS_SECRET)
	
	twitter_trends = twitter_api.GetTrendsCurrent()
	for trend in twitter_trends:
		# print trend.name
		hashtag = trend.name
		Search(hashtag.replace('#',''))

def tweepy_trend_hashtag():
	auth = tweepy.OAuthHandler(consumer_key=CONSUMER_KEY,consumer_secret=CONSUMER_SECRET)
	auth.set_access_token(ACCESS_TOKEN,ACCESS_SECRET)

	api = tweepy.API(auth)
	trends1 = api.trends_place(1)

	hashtags = [x['name'] for x in trends1[0]['trends']]

	for tags in hashtags:
		Search(re.sub("#","",tags))

def Search(query):
	key = 'AIzaSyDxHeNi6StT62JnwaKh36LFqSnN-VMpUL8'
	# query = raw_input("Enter query : ")
	# query_search = urllib.urlencode({query})
	# libraryRestrict = raw_input("Restrict search : ") 
	# orderBy = raw_input("orderBy (relevance/newest)")
	# printType = raw_input("PrintType(books/magazines) : ")
	# maxResults = raw_input("Results (max 40) : ")


	# url ='https://www.googleapis.com/books/v1/volumes?q=%s&key=%s&libraryRestrict=no-restrict&orderBy=relevance&printType=all&maxResults=40' %(query,key,libraryRestrict,orderBy,printType,maxResults)
	
	url ='https://www.googleapis.com/books/v1/volumes?q=%s&key=%s&libraryRestrict=no-restrict&orderBy=relevance&printType=all&maxResults=40' %(query,key)
	# search_results = urllib.urlopen(url).read()
	search_url = urllib.urlopen(url)

	results  = json.loads(search_url.read())
	print results
	# for res in results['items']:
	# 	print res['volumeInfo']['title'] + " : "
	# 	# if 'industryIdentifiers' in res['volumeInfo']:
	# 	# 	if res['volumeInfo']['industryIdentifiers'][0]['type'] == "ISBN_13"
	# 	# 	print '\t' + '\t' + '\t' + ""res['volumeInfo']['industryIdentifiers'][0]['identifier']
	# 	# else:
	# 	# 	print
	# 	# print '\t' + res['volumeInfo']['averageRating']
	# 	if 'authors' in res['volumeInfo']:
	# 		print '\t' + '\t' + '\t' + res['volumeInfo']['authors'][0]
	# 	else:
	# 		pass