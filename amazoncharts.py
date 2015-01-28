# -*- coding: utf-8 -*-
from BeautifulSoup import BeautifulSoup
from pymongo import MongoClient
import urllib2
import requests
import re
import time

# def removeNonAscii(s): return "".join(i for i in s if ord(i)<128)

class GetAmazonCharts():

    def getAllAmazonKindleTops(self):

        client = MongoClient()
        post = client['amazoncharts']['topchart']
        # print post


        proxy = urllib2.ProxyHandler({'http': 'http://myproxy:80'})
        opener = urllib2.build_opener(proxy)
        urllib2.install_opener(opener)

        #url of paid books
        # base_url="http://www.amazon.com/Best-Sellers-Kindle-Store-%s/zgbs/digital-text/154607011/ref=zg_bs_nav_kstore_2_154606011#"

        #url of free books
        base_url="http://www.amazon.com/Best-Sellers-Kindle-Store-%s/zgbs/digital-text/154607011/ref=zg_bs_nav_kstore_2_154606011?_encoding=UTF8&tf=1#"

        url_art = [ base_url%"Arts-Photography" + str(i) for i in range(1, 6)]
        url_bio = [base_url%"Biography-Memoirs" + str(i) for i in range(1, 6)]
        url_biz = [base_url%"Business-Investing" + str(i) for i in range(1, 6)]
        url_child = [base_url%"Childrens-eBooks" + str(i) for i in range(1, 6)]
        url_comic = [base_url%"Comics-Graphic-Novels" + str(i) for i in range(1, 6)]
        url_computer = [base_url%"Computers-Technology" + str(i) for i in range(1, 6)]
        url_crime = [base_url%"Thriller-Suspense" + str(i) for i in range(1, 6)]
        url_cookbook = [base_url%"Cookbooks-Food-Wine" + str(i) for i in range(1, 6)]
        url_crafts = [base_url%"Crafts-Hobbies-Home" + str(i) for i in range(1, 6)]
        url_education = [base_url%"Education-Teaching" + str(i) for i in range(1, 6)]
        url_lgbt = [base_url%"Gay-Lesbian" + str(i) for i in range(1, 6)]
        url_health = [base_url%"Health-Fitness-Dieting" + str(i) for i in range(1, 6)]
        url_history = [base_url%"History" + str(i) for i in range(1, 6)]
        url_humor = [base_url%"Humor-Entertainment" + str(i) for i in range(1, 6)]
        url_literature = [base_url%"Literature-Fiction" + str(i) for i in range(1, 6)]
        url_nonfiction = [base_url%"Nonfiction" + str(i) for i in range(1, 6)]
        url_parenting = [base_url%"Parenting-Relationships" + str(i) for i in range(1, 6)]
        url_politics = [base_url%"Politics-Social-Sciences" + str(i) for i in range(1, 6)]
        url_professional = [base_url%"Professional-Technical" + str(i) for i in range(1, 6)]
        url_reference = [base_url%"Reference-eBooks" + str(i) for i in range(1, 6)]
        url_religion = [base_url%"Religion-Spirituality" + str(i) for i in range(1, 6)]
        url_romance = [base_url%"Romance" + str(i) for i in range(1, 6)]
        url_science_math = [base_url%"Science-Math" + str(i) for i in range(1, 6)]
        url_science_fiction = [base_url%"Science-Fiction-Fantasy" + str(i) for i in range(1, 6)]
        url_self_help = [base_url%"Self-Help" + str(i) for i in range(1, 6)]
        url_sports = [base_url%"Sports-Outdoors" + str(i) for i in range(1, 6)]
        url_teen_young = [base_url%"Teen-Young-Adult-eBooks" + str(i) for i in range(1, 6)]
        url_travel = [base_url%"Travel" + str(i) for i in range(1, 6)]
        url_foreign_language = [base_url%"Foreign-Language-eBooks" + str(i) for i in range(1, 6)]

        # mongo = dbFunctions()

        # url_all = [url_art , url_bio, url_biz, url_child, url_comic, url_computer, url_crime]
        url_all = {
                    'Art' : url_art,
                    'Biography' : url_bio,
                    'Business' : url_biz,
                    'Children' : url_child,
                    'Comic': url_comic,
                    'Computer' : url_computer,
                    'Crime': url_crime,
                    'Cookbooks' : url_cookbook,
                    'Crafts' : url_crafts,
                    'Education' : url_education,
                    'Gay_Lesbian' : url_lgbt,
                    'Health' : url_health,
                    'History': url_history,
                    'Humor' : url_humor,
                    'Literature' : url_literature,
                    'Non_Fiction': url_nonfiction,
                    'Parenting' : url_parenting,
                    'Politics': url_politics,
                    'Professional_Technical' : url_professional,
                    'Refrence' : url_reference,
                    'Religion' : url_religion,
                    'Romance': url_romance,
                    'Science_Math' : url_science_math,
                    'Science_Fiction' : url_science_fiction,
                    'Self_Help': url_self_help,
                    'Sports' : url_sports,
                    'Teen_Young' : url_teen_young,
                    'Travel' : url_travel,
                    'Foreign_Language' : url_foreign_language
                   }

        entry = []

        for url_section in url_all.keys():
            print 20 * '-' + url_section + 20 * '-'
            for url in url_all[url_section]:
                soup = BeautifulSoup(requests.get(url).text)
                best_sellers = soup.findAll('div', {'class':'zg_itemImmersion'})
                for bs in best_sellers:
                    rank = bs.find('div', {'class':'zg_rankDiv'}).span.string.replace('.', '').encode('utf-8')
            #       print rank
                    try:
                        title_short = bs.find('div', {'class':'zg_title'}).a.string
                        title_link = re.sub('\s+', '', bs.find('div', {'class':'zg_title'}).a['href'])
                        # page_title = urllib2.urlopen(title_link)
                        soup_title = BeautifulSoup( requests.get( title_link).text)
                        title_full = soup_title.find('span', {'id' : 'btAsinTitle'}).contents[0].encode('utf-8')
                    except:
                        title_short = 'Unknown title'
                        title_full = 'Unknown title'
                    try:
                        author_unf = bs.find('div', {'class':'zg_byline'}).string.replace('by ', '')[:-1]
                        author = re.sub('\s+', ' ', author_unf).encode('utf-8')
      #                 print author
                    except:
                        author = 'Unknown author'
                    try:
                        rate_url = bs.find('span', {'class' : 'asinReviewsSummary'}).span['title'].string
                        print "rate_url :" + rate_url
                        # rater = rate_url.find('span',{'class' : 'swSprite'}).span.string
            #           print rate
                    except:
                        rate = 'No rating'
                        # print "asdadas"
                    try:
                        price = bs.find('div', {'class':'zg_price'}).strong.string.encode('utf-8')
            #           print price
                    except:
                        price = 'Unknown price'
                    try:
                        image_link = bs.find('div', {'class' : 'zg_itemImageImmersion'}).img['src'].encode('utf-8')
                    except:
                        image_link = 'Not Found'
                    data = { 
                            'category' : url_section,
                            'rank' : rank , 
                            'title':title_full,
                            'short_title': title_short.encode('utf-8'),
                            'title_link': title_link.encode('utf-8'),
                            'author': author,
                            'rate': rate,
                            'price' : price,
                            'image_link' : image_link
                            }

                    post.update(
                        {"book_type" : "kindle book"},
                        {"$push" : {
                        "book_details" : {
                        "category" : url_section,
                        "rank" : rank , 
                        "title":title_full,
                        "short_title": title_short.encode('utf-8'),
                        "title_link": title_link.encode('utf-8'),
                        "author": author,
                        "rate": rate,
                        "price" : price,
                        "image_link" : image_link
                         } } }
                        )

                    # print data

                    entry.append(data)
            time.sleep(300)

        collect = {
                    "entry" : entry
                    }
        
        # post.insert(entry)

                #    mongo.insertItemtoCharts(entry)
                    
if __name__ == '__main__':
    ch = GetAmazonCharts()
    ch.getAllAmazonKindleTops()