#sudo pip instal flask,pymongo
import json
from flask import Flask
from pymongo import MongoClient
from library import getCollection,helloWorld

app = Flask(__name__)

@app.route('/hello')
def hello():
    return helloWorld()


@app.route('/getTweet/')
def getTweet():
    collection = getCollection('Adonis')
    json = collection.find_one( { 'checked' : {'$exists' : False } })
    #result = collection.update( { 'checked' : {'$exists' : False } }, { '$set' : {'checked' : True}})
    tweet = {}
    if json:
        tweet = {
            "id" : json['id'],
            "text" : unicode(json['text']),
            "collection" : "Adonis"
            }
    #dat = tweet.json()
    print tweet
    #print dat
    #return flask.jsonify(**dat)
    tw = json.dumps(tweet)
    return tw

@app.route('/deleteTweet/<id>')
def deleteTweet(id):
    #?? na prosthesw na pairnei kai to collection pou theloume
    collection = getCollection('Adonis')
    json = collection.find_one({"id" : float(id)})
    if json:
        print '<$>yeah i found it !'
        collection.remove({"id" : float(id)})
    else:
        print '<$>already deleted !'
    return '', 200



if __name__ == '__main__':
    app.debug = True
    app.run()
