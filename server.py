#final
#sudo pip instal flask,pymongo
import json
import flask
from flask import Flask
from pymongo import MongoClient
from library import getCollection,helloWorld

app = Flask(__name__)

@app.route('/hello')
def hello():
    return helloWorld()


@app.route('/getTweet/<col>')
def getTweet(col):
    collection = getCollection(col)
    json = collection.find_one( { 'checked' : {'$exists' : False } })

    tweet = {}
    if json:
        tweet = {
            "id" : repr(json['id']),
            "text" : json['text'].encode('utf-8'),
            "collection" : col
            }
    print tweet['id']
    return flask.jsonify(**tweet)

@app.route('/deleteTweet/<id>&<col>')
def deleteTweet(id,col):

    collection = getCollection(col)
    idv = float(id)
    json = collection.find_one({"id" : idv})
    if json:
        print '<$>yeah i found it !'
        collection.remove({"id" : idv})
    else:
        print '<$>doesnt exist anymore!'
    return '', 200

@app.route('/decideTweet/<id>&<col>&<sign>')
def decideTweet(id,col,sign):
    collection = getCollection(col)
    idv = float(id)
    json = collection.find_one_and_update( { 'id': idv}, { '$set': {'checked' : True}} )
    print 'flag123'
    if json:
        # if the object still exists (in case simultaneously somebody deleted it)
        print 'flag'
        collection = getCollection('Results')
        result = collection.insert({'id' : json['id'], 'text' : json['text'], 'sign' : sign})
    return '',200



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
