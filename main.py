#mongoBD
import pymongo
import sys

print "Encymon"

#read the database file configuration 
try: 
	configDataBase = open("./config.database.txt","r")
except: 
	print "I can't open ./config.database.txt"
	print "Can you verify if it's created !"

#opendatabase connection
client = pymongo.MongoClient(configDataBase.read())
db = client.test

#collection = db.test_collection

#print collection
print "end"