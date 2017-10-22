from flask import Flask
from flask import render_template
import stochastic_sampling
import tokenize_corpus
import os
import markov
import requests
import json
from pprint import pprint
app = Flask(__name__)


@app.route('/')
def hello_world():
    fh = tokenize_corpus.tokenize('./corpus.txt')
    markov_chain_var = markov.markov_chain_2nd_order(fh)
    weighted = markov.weighted_markov(markov_chain_var)
    sentence = markov.walk_the_markov(weighted)
    return render_template('index.html', sentence=sentence)
    

if __name__ == '__main__':
    app.run()
