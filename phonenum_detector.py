import sys
import re
import MySQLdb
import Tkinter, tkFileDialog


even_list = ['0','2','4','6','8']
odd_list = ['1','3','5','7','9']

global isd_code,num_as_str,number



db= MySQLdb.connect(host="localhost",user="root",passwd="lucifer-666",db="phone_detect")
cursor = db.cursor()

def find_length(number):
	if len(number) == 10:
		isd_code = number[:2]

		select_insert_query(isd_code,number)
	elif len(number) == 11:
		# North American Numbering Plan
		if number[0] == '1':
			isd_code = nanp(number)
			select_insert_query(isd_code,number)
		else:
			isd_code_1 = number[:2]
			select_insert_query(isd_code_1,number)
			isd_code_2 = number [:3]
			select_insert_query(isd_code_2,number)

	elif len(number) == 12:
		isd_code_3 = number[:2]
		isd_code_4 = number [:3]

		select_insert_query(isd_code_3,number)
		select_insert_query(isd_code_4,number)

def nanp(numb):
	na_code = None  
	# print numb
	code = numb[:4]
	if code[1] in odd_list:
		if code[2] in odd_list:
			na_code = code
			# print na_code
		elif code[2] in even_list:
			if code[3] in even_list:
				na_code = code
				# print na_code
			elif code[3] in odd_list:
				na_code = code
				# print na_code
			else:
				print "NOT FOUND"
	elif code[1] in even_list:
		if code[2] in even_list:
			if code[3] in even_list:
				na_code = code
				# print na_code
			elif code[3] in odd_list:
				na_code = code
				# print na_code
			else:
				print "NOT FOUND"
		elif code[2] in odd_list:
			if code[3] in odd_list:
				na_code = code
				# print na_code
			elif code[3] in even_list:
				na_code = code
				# print na_code
			else:
				print "NOT FOUND"
	else:
		print "NOT FOUND"

	nan_query = """SELECT COUNT(1) FROM country WHERE phonecode = '%s'; """ %(na_code)
	cursor.execute(nan_query)
	if cursor.fetchone()[0]:
		# print na_code
		return na_code
	else:
		na_code = numb[0]
		# print na_code
		return na_code

def select_insert_query(isd_code,phonenumber):

	# db= MySQLdb.connect(host="localhost",user="root",passwd="lucifer-666",db="phone_detect")
	# cursor = db.cursor()

	query = """ SELECT `name`,`iso3` FROM `country` WHERE `phonecode` = '%s' ORDER BY `name` ASC;""" %(isd_code)
	cursor.execute(query)
	data = cursor.fetchall()

	for row in data:
		query_sort = """INSERT INTO `sorted_no`(`phonenumber`,`name`,`iso3`) VALUES ('%s','%s','%s') ;""" %(phonenumber,row[0],row[1])
		cursor.execute( query_sort )
		db.commit()
		# print query_sort

root = Tkinter.Tk()
root.withdraw()
file_path = tkFileDialog.askopenfilename()
with open(file_path,"r") as f:
	for line in f:
		# print line
		num_as_str = re.sub(r'\W+', '', line)
		# print num_as_str
		# find_length(num_as_str)
		# num_as_str = re.sub(r"\b0{2}","",num_as_str)
		num_as_str = re.sub("^00","",num_as_str)
		find_length(num_as_str)

cursor.close()
f.close()
db.close()