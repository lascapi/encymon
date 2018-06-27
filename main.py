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

#read the xml file (little local database) 
try: 
	xmlFile = open("./database.xml","r")
except: 
	print "I can't open ./database.xml"
	print "Can you verify if it created !"

#opendatabase connection
client = pymongo.MongoClient(configDataBase.read())

#db = client.test
#collection = db.test_collection

db = client.peoples
collection_stars = db.stars


print "db ==================="
print db
print "collection ================"
print collection_stars
print "item count ==============="
print collection_stars.count()

#item = collection.insert_one({"test":"1"}).inserted_id
#print "item ============"
#print item

#for item in collection.find():
#	print item

client.close()
print "end"