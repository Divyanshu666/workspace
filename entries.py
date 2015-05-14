import MySQLdb
import random
import string
from pymongo import MongoClient


# MySQL function

db= MySQLdb.connect(host="localhost",user="root",passwd="lucifer-666",db="test_db")

cursor=db.cursor()


# # sql="""CREATE TABLE employee(name CHAR(20) NOT NULL,
# # 	role CHAR(10),
# # 	unit CHAR(10))
# # """
# count = 0
# while (count < 10000):
# 	name=''.join(random.sample(string.lowercase,6))
# 	phone = random.randint(9,999999999)
# 	sex = random.choice(['m','f'])
	
	sql=""" INSERT INTO test_sql(name,phn,sex)
	VALUES('%s','%s','%s')"""%(name,phone,sex)
	count =count +1
	print count
	print phone
	# print sex
	cursor.execute(sql)
db.commit()
try:
	cursor.execute(sql)
	db.commit()
except:
	db.rollback()

# cursor.fetchall()

# # for row in cursor:
# # 	print row

db.close()

MongoDB function

mongodb connection

client = MongoClient()

# connection to mongodb database

db=client.detect_phone  

# connection to mongodb collection

collection=db.mycoll


# insert data into mongodb

i = 0
while (i < 100):
	name=''.join(random.sample(string.lowercase,6))
	phone = random.randint(9,999999999)
	sex = random.choice(['m','f'])
	
	post={
		"name" : name,
  		"phone" : phone,
  		"sex" : sex
	}
	collection.insert(post)

