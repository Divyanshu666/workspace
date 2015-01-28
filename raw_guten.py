ebook_base = "http://www.gutenberg.org/ebooks/"

online_html = "http://www.gutenberg.org/files/" 2000/2000-h/2000-h.htm

epub_ebook_url_collect = [ ebook_base + str(i) + ".epub.noimages" for i in xrange(10) ]
mobi_ebook_url_collect = [ ebook_base + str(i) + ".kindle.noimages" for i in xrange(49999) ]
text_ebook_url_collect = [ ebook_base + str(i) + ".txt.utf-8" for i in xrange(49999) ]

data_epub = {}
data_mobi = {}
data_text = {}

format = []

for i in xrange(10):
	epub_ebook_url = ebook_base + str(i) + ".epub.noimages"
	mobi_ebook_url = ebook_base + str(i) + ".kindle.noimages"
	text_ebook_url = ebook_base + str(i) + ".txt.utf-8"

	epub_ebook_url_collect.append(epub_ebook_url)
	mobi_ebook_url_collect.append(mobi_ebook_url)
	text_ebook_url_collect.append(text_ebook_url)

#read online
for i in xrange(10):
	online_book_url = online_html + str(i) +"/" + str(i) + "-h" + "/" + str(i) + "-h.htm"


#for line in epub_ebook_url_collect:


import glob

bookpath = '/home/cyph3r/Desktop/cache/epub/*/*'
for filename in glob.glob(book_path):
	#filename will print the every filename path inside epub folder
	print filename 



