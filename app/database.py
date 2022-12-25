import pymongo as pmon
# mongo_url ="mongodb+srv://bcadmin:T7WWCjIAXmY0NHbW@cluster1.5u9wi63.mongodb.net/?retryWrites=true&w=majority"
mongo_url = "mongodb+srv://bcadmin:T7WWCjIAXmY0NHbW@cluster1.5u9wi63.mongodb.net/test"
client = pmon.MongoClient(mongo_url)
dbase = client['bcentraldb']