import json
import urllib
import requests
import twitter
import googlemaps
import tweepy
import re


def search():
	key = 'AIzaSyBH6TFovmncqKM1mwDJ6lUE7L2oqRAL8dM'

	query = raw_input("Enter query : ")
	# query_search = urllib.urlencode({query})
	libraryRestrict = raw_input("Restrict search : ") 
	orderBy = raw_input("orderBy (relevance/newest) : ")
	printType = raw_input("PrintType(books/magazines) : ")
	maxResults = raw_input("Results (max 40) : ")

	url ='https://www.googleapis.com/books/v1/volumes?q=%s&key=%s&libraryRestrict=%s&orderBy=%s&printType=%s&maxResults=%s' %(query,key,libraryRestrict,orderBy,printType,maxResults)

	search_url = urllib.urlopen(url)
	results  = json.loads(search_url.read())
	# print results
	# print results
	google_book_search = []
	# for res in results['items']:
	# 	print res['volumeInfo']

	query_book_data = [ {
							'book_title':res['volumeInfo']['title'].encode('utf-8'),
							# 'subtitle':res['volumeInfo']['subtitle'].encode('utf-8'),
							'author':res['volumeInfo']['authors'][0],
							'ratings':res['volumeInfo']['averageRating'],
							'pages':res['volumeInfo']['pageCount'],
							'thumbnail':res['volumeInfo']['imageLinks']['thumbnail'],
							'category':res['volumeInfo']['categories'][0]

						}
						for res in results['items'] if 'authors' in res['volumeInfo']]

	test = {
		"data": query_book_data
	}
	print test
	
# def twitter_trend_hashtag():

# 	CONSUMER_KEY = 'bhipusATdYgFpi9W2nCaHK57c'
# 	CONSUMER_SECRET = 'XwTylNDMSogXIMhKEwc5uaSPTcyYkTDbfHj6ZifWxZu3oLl0RJ'
# 	ACCESS_TOKEN = '994668080-T9nQ2EH6LBZFeND2HKJ0mfcj0Zm5lUZ57uSNQ0Hx'
# 	ACCESS_SECRET = '72ppPOwj3vZtetdZXTLm8YSv3ZCCId0w1rEIQloBR8VQx'

# 	# url = 'https://api.twitter.com/1.1/trends/place.json?id=1'

# 	twitter_api = twitter.Api(consumer_key=CONSUMER_KEY,consumer_secret=CONSUMER_SECRET,access_token_key=ACCESS_TOKEN,access_token_secret=ACCESS_SECRET)
# 	twitter_trends = twitter_api.GetTrendsCurrent()
# 	for trend in twitter_trends:
# 		# print trend.name
# 		hashtag = trend.name
# 		hashtag = hashtag.replace('#','').encode('utf-8')
# 		# print hashtag
# 		google_book_search(hashtag)

# def detect_woeid():

# 	woeid_data = {}

# 	for details in tweepy_trends:
# 		woeid_data[details['name']] = details['woeid']

# 	place = raw_input("Select Place(worldwide/country_name/city_name) : ")
# 	return woeid_data.get(place)	

def tweepy_trend_hashtag():
	CONSUMER_KEY = 'bhipusATdYgFpi9W2nCaHK57c'
	CONSUMER_SECRET = 'XwTylNDMSogXIMhKEwc5uaSPTcyYkTDbfHj6ZifWxZu3oLl0RJ'
	ACCESS_TOKEN = '994668080-T9nQ2EH6LBZFeND2HKJ0mfcj0Zm5lUZ57uSNQ0Hx'
	ACCESS_SECRET = '72ppPOwj3vZtetdZXTLm8YSv3ZCCId0w1rEIQloBR8VQx'
	
	auth = tweepy.OAuthHandler(consumer_key=CONSUMER_KEY,consumer_secret=CONSUMER_SECRET)
	auth.set_access_token(ACCESS_TOKEN,ACCESS_SECRET)
	api = tweepy.API(auth)

	woeid_data = {}

	woeid_available = api.trends_available()

	for details in woeid_available:
		woeid_data[details['name']] = details['woeid']

	world_places = raw_input("Select Place(worldwide/country_name/city_name) : ")

	if world_places == None:
		tweepy_trends = api.trends_place( 1 )
		tweepy_hashtags = [x['name'] for x in tweepy_trends[0]['trends']]
		for tags in tweepy_hashtags:
			tags = re.sub("#","",tags)
			google_book_search(tags)
	else:
		tweepy_trends = api.trends_place( woeid_data.get(world_places) )
		tweepy_hashtags = [x['name'] for x in tweepy_trends[0]['trends']]
		for tags in tweepy_hashtags:
			tags = re.sub("#","",tags)
			# print tags
			google_book_search(tags)

# def unique_hashtags():


def google_book_search(query):
	key = 'AIzaSyBH6TFovmncqKM1mwDJ6lUE7L2oqRAL8dM'

	url ='https://www.googleapis.com/books/v1/volumes?q=%s&key=%s&libraryRestrict=no-restrict&orderBy=relevance&printType=books&maxResults=40' %(query,key)
	# search_results = urllib.urlopen(url).read()
	search_url = urllib.urlopen(url)
	results  = json.loads(search_url.read())
	# print results
	google_book_search = []
	if "items" in results.keys(): 
		for res in results['items']:
			if 'authors' in res['volumeInfo']:
				if 'averageRating' in res['volumeInfo']:
					if 'pageCount' in res['volumeInfo']:
						if 'categories' in res['volumeInfo']:
							if 'imageLinks' in res['volumeInfo']:
								data= {
										'book_title':res['volumeInfo']['title'].encode('utf-8'),
										# 'subtitle':res['volumeInfo']['subtitle'].encode('utf-8'),
										'author':res['volumeInfo']['authors'][0],
										'ratings':res['volumeInfo']['averageRating'],
										'pages':res['volumeInfo']['pageCount'],
										'thumbnail':res['volumeInfo']['imageLinks']['thumbnail'],
										'category':res['volumeInfo']['categories'][0]

									}
							else:
								data= {
										'book_title':res['volumeInfo']['title'].encode('utf-8'),
										# 'subtitle':res['volumeInfo']['subtitle'].encode('utf-8'),
										'author':res['volumeInfo']['authors'][0],
										'ratings':res['volumeInfo']['averageRating'],
										'pages':res['volumeInfo']['pageCount'],
										'category':res['volumeInfo']['categories'][0]

									}
						else:
							data= {
									'book_title':res['volumeInfo']['title'].encode('utf-8'),
									# 'subtitle':res['volumeInfo']['subtitle'].encode('utf-8'),
									'author':res['volumeInfo']['authors'][0],
									'ratings':res['volumeInfo']['averageRating'],
									'pages':res['volumeInfo']['pageCount'],
									'thumbnail':res['volumeInfo']['imageLinks']['thumbnail'],
								}
					else:
						data= {
								'book_title':res['volumeInfo']['title'].encode('utf-8'),
								# 'subtitle':res['volumeInfo']['subtitle'].encode('utf-8'),
								'author':res['volumeInfo']['authors'][0],
								'ratings':res['volumeInfo']['averageRating'],
								'thumbnail':res['volumeInfo']['imageLinks']['thumbnail'],
								'category':res['volumeInfo']['categories'][0]
							}
				else:
					data= {
							'book_title':res['volumeInfo']['title'].encode('utf-8'),
							# 'subtitle':res['volumeInfo']['subtitle'].encode('utf-8'),
							'author':res['volumeInfo']['authors'][0],
							'pages':res['volumeInfo']['pageCount'],
							'thumbnail':res['volumeInfo']['imageLinks']['thumbnail'],
							# 'category':res['volumeInfo']['categories'][0]
						}
			else:
				data= {
						'book_title':res['volumeInfo']['title'].encode('utf-8'),
						# 'subtitle':res['volumeInfo']['subtitle'].encode('utf-8'),
						'ratings':res['volumeInfo']['averageRating'],
						'pages':res['volumeInfo']['pageCount'],
						'thumbnail':res['volumeInfo']['imageLinks']['thumbnail'],
						'category':res['volumeInfo']['categories'][0]

					}
			google_book_search.append(data)
	
	test = {
		"data": google_book_search
	}
	print test
	return {
		"data": google_book_search
	} 

if __name__ == "__main__":
	# twitter_trend_hashtag()
	tweepy_trend_hashtag()
	search()