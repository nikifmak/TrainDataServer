from pymongo import MongoClient

def helloWorld():
    return 'hello world'

def getCollection(col):
    try:
        client = MongoClient('localhost', 27017)
        print "Connected successfully!!!"
    except pymongo.errors.ConnectionFailure, e:
        print "Could not connect to MongoDB: %s" % e
    db = client.database
    collection = db[col]
    return collection
