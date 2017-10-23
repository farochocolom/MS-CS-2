from flask import Flask, request, make_response, redirect
from flask_restful import Api
from flask import render_template
from pymongo import MongoClient
import tokenize_corpus
import markov


app = Flask(__name__)
# app.config.from_pyfile('config.cfg')
mongo = MongoClient('mongodb://Specialist17:darkknight17@ds227555.mlab.com:27555/tweet_gen')
app.db = mongo.tweet_gen
api = Api(app)


@app.route('/')
def hello_world():
    fh = tokenize_corpus.tokenize('./corpus.txt')
    markov_chain_var = markov.markov_chain_2nd_order(fh)
    weighted = markov.weighted_markov(markov_chain_var)
    sentence = markov.walk_the_markov(weighted)
    return render_template('index.html', sentence=sentence)


@app.route('/favorites', methods=['POST', 'GET'])
def favorites():
    favorites_col = app.db.favorites
    if request.method == 'POST':
        sentence = request.form['sentence']
        favorites_col.insert_one({'sentence': sentence})
        return redirect('/')
    else:
        favorites = favorites_col.find()
        fav_array = []
        for favorite in favorites:
            fav_array.append(favorite)
        return render_template('favorites.html', favorites=fav_array)


#  Custom JSON serializer for flask_restful
@api.representation('application/json')
def output_json(data, code, headers=None):
    resp = make_response(JSONEncoder().encode(data), code)
    resp.headers.extend(headers or {})
    return resp


if __name__ == '__main__':
    app.run()
