from flask import Flask
from flask import render_template
import stochastic_sampling
from Tweet_Generator import markov, tokenize
import os
import requests
import json
from pprint import pprint
app = Flask(__name__)


@app.route('/')
def hello_world():
    fh = tokenize.tokenize('./corpus.txt')
    markov_chain_var = markov.markov_chain_2nd_order(fh)
    weighted = markov.weighted_markov(markov_chain_var)
    # pprint(weighted)
    sentence = markov.walk_the_markov(10, weighted)
    return render_template('index.html', sentence=sentence)


@app.route('/corpus_creator')
def create_the_corpus():

    file_to_read = open("./pages.txt", "r")
    file_to_write = open("./corpus.txt", "w")
    read_file = file_to_read.read()
    page_list = read_file.split()

    for page in page_list:
        print(page)
        resp = requests.get("https://api.diffbot.com/v3/article?token=257975cb7afce09e99c068569f3f19fa&url="+page)
        sentence = resp.content.decode()
        # print(sentence)
        text = json.loads(sentence)
        file_to_write.write(text['objects'][0]['text'])

    file_to_write.close()

    # file_to_read = open("./pages.txt", "r")
    # read_file = file_to_read.read()
    # page_list = read_file.split()
    # print(page_list)
    #
    # resp = requests.get("https://api.diffbot.com/v3/article?token=257975cb7afce09e99c068569f3f19fa&url=https://www.scienceofpeople.com/2017/09/what-is-an-intrapreneur/")
    # # sentence = resp.content
    # sentence = resp.content.decode()
    # text = json.loads(sentence)
    return "tamo xóticos"
    # return render_template('index.html', sentence=sentence)


if __name__ == '__main__':
    app.run(debug=True)
