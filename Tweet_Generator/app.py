from flask import Flask
from flask import render_template
import markov
import tokenize
import os
import requests

app = Flask(__name__)


@app.route('/')
def hello_world():
    # dirpath = os.getcwd()
    # word_file = stochastic_sampling.process_histogram_without_numbers(
    #     dirpath+"/SoP.txt")
    word_file = tokenize.tokenize('./SoP.txt')

    # sentence = stochastic_sampling.create_random_sentence(10, word_file)

    markov_chain_var = markov.markov_chain(word_file)
    weighted = markov.weighted_markov(markov_chain_var)
    sentence = markov.walk_the_markov(15, weighted)

    return render_template('index.html', sentence=sentence)


# @app.route('/<int:num>')
# def sentence_with_num_of_words(num):
#     dirpath = os.getcwd()
#     word_file = stochastic_sampling.process_histogram_without_numbers(
#         dirpath+"/output.txt")
#
#     sentence = stochastic_sampling.create_random_sentence(num, word_file)
#
#     return render_template('index.html', sentence=sentence)


@app.route('/corpus_creator')
def create_a_corpus(num):
    file_to_read = open(source_text, "r")
    read_file = file_to_read.read()
    # response = requests.get("https://api.diffbot.com/v3/article?token=257975cb7afce09e99c068569f3f19fa&url=https:%2F%2Fwww.scienceofpeople.com%2F2017%2F09%2Fwhat-is-an-intrapreneur%2F")
    print("https://api.diffbot.com/v3/article?token=257975cb7afce09e99c068569f3f19fa&url=https:%2F%2Fwww.scienceofpeople.com%2F2017%2F09%2Fwhat-is-an-intrapreneur%2F")
    # return render_template('index.html', sentence=response)


if __name__ == '__main__':
    app.run(debug=True)
