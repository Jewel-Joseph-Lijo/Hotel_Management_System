#Establishing Database Connection
import pymongo

myclient = pymongo.MongoClient("YourPortName")
mydb = myclient["YourDatabaseName"]
mycol = mydb["YourFirstCollectionName"]
mycol2=mydb["YourSecondCollectionName"]
