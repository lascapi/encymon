#mongoBD
import pymongo
import sys

print "Encymon"

#test for pymongo's version
if pymongo.__version__ == "3.4.0":
	print "Good version => pymongo 3.4.0"
else: 
	print "pymongo 3.4.0 require. You have pymongo " + pymongo.__version__

#read the database file configuration 
try: 
	configDataBase = open("./config.database.txt","r")
except: 
	print "I can't open ./config.database.txt"
	print "Can you verify if it created !"

#opendatabase connection
client = pymongo.MongoClient(configDataBase.read())
db = client.test

#collection = db.test_collection

#print collection
print "end"