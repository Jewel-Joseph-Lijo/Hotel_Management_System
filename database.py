#Establishing Database Connection
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Hotel"]
mycol = mydb["customers"]
mycol2=mydb["vacated_customers"]