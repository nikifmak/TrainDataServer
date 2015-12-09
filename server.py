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
    print 'ehreherrehrh'
    print idv
    print type(idv)
    json = collection.find_one({"id" : idv})
    print json
    if json:
        print '<$>yeah i found it !'
        collection.remove({"id" : idv})
    else:
        print '<$>doesnt exist anymore!'
    return '', 200

@app.route('/decideTweet/<id>&<sign>')
def decideTweet(id,sign):
    collection = getCollection('Adonis')
    json = collection.find_one_and_update( { 'id': float(id)}, { '$set': {'checked' : True}} )
    if json:
        # if the object still exists (in case simultaneously somebody deleted it)
        collection = getCollection('Results')
        result = collection.insert({'id' : json['id'], 'text' : json['text'], 'sign' : sign})
    return '',200



if __name__ == '__main__':
    app.debug = True
    app.run()
