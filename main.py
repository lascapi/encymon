#mongoBD
import pymongo
import sys
import os
import ssl

print "Encymon"

#test for pymongo's version
if pymongo.__version__ == "3.4.0":
	print "pymongo's version 3.4.0, done"
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
#db = client.test

#collection = db.test_collection

db = client.get_default_database()

print db

print db.collection_names()


#for item in collection.find():
#	print item

print "end"