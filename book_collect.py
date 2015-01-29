import json
import urllib
import requests
from pymongo import MongoClient



# def database_con():

def book_collect():

	client = MongoClient()
	db = client['google_books_data']
	collection = db['books_collect']


	book_category = [
		'Biographies & Memoirs','Buisness & Investing','Children Books',
		'Cooking,Food & Wine','Engineering',
		'Fiction & Literature','Health ,Mind & Body',
		'History','Religion & Spirituality','Romance'
	]

	for book_cat in book_category:
		query = book_cat
		# print query

		key = 'AIzaSyBH6TFovmncqKM1mwDJ6lUE7L2oqRAL8dM'
		url ='https://www.googleapis.com/books/v1/volumes?q=%s&key=%s&libraryRestrict=no-restrict&orderBy=relevance&printType=books&maxResults=40' %(query,key)

		search_url_data = requests.get(url).json()
		# results  = json.loads(search_url.read())

		test_keys=['publisher','title','authors','averageRating','pageCount','imageLinks','categories','industryIdentifiers']
		query_book_data = []
		data = {}
		for res in search_url_data['items']:
			# print res['volumeInfo']
			for keys in test_keys:
				# print keys
				if keys in res['volumeInfo'].keys():

					try:
						publisher = res['volumeInfo']['publisher']
					except:
						publisher = 'unknown_publisher'
					try:
						book_title = res['volumeInfo']['title']
					except:
						book_title = 'unknown_title'

					try:
						authors = res['volumeInfo']['authors']
					except:
						authors = 'unknown_author'

					try:
						ratings = res['volumeInfo']['averageRating']
					except:
						ratings = 'no_ratings'

					try:
						pages = res['volumeInfo']['pageCount']
					except:
						pages = 'unknown_count'

					try:
						thumbnail = res['volumeInfo']['imageLinks']
					except:
						thumbnail = 'no_thumbnail'

					try:
						category = res['volumeInfo']['categories'][0]
					except:
						category = 'unknown_category'

					try:
						ISBN = res['volumeInfo']['industryIdentifiers']
					except:
						ISBN = 'no_ISBN'

					data = {
							'book_title':book_title.encode('utf-8'),
							'authors':authors,
							'publisher' : publisher.encode('utf-8'),
							'ratings':ratings,
							'pages':pages,
							'thumbnail':thumbnail,
							'category':category.encode('utf-8'),
							'ISBN' : ISBN
						}

					# if ( collection.find( {"category" : { $in : category }} ) ):
					# 	collection.update ( 
					# 			{ "category" : category},
					# 			{"$push" : {

					# 			} }
					# 		)
			print data


	# query_book_data = [ {
	# 						'book_title':res['volumeInfo']['title'].encode('utf-8'),
	# 						# 'subtitle':res['volumeInfo']['subtitle'].encode('utf-8'),
	# 						'author':res['volumeInfo']['authors'][0],
	# 						'ratings':res['volumeInfo']['averageRating'],
	# 						'pages':res['volumeInfo']['pageCount'],
	# 						'thumbnail':res['volumeInfo']['imageLinks']['thumbnail'],
	# 						'category':res['volumeInfo']['categories'][0]
	# 					}
	# 					for res in results['items'] if 'authors' in res['volumeInfo']
	# 				]
	# print  query_book_data

if __name__== '__main__':
	book_collect()