from flask import Flask
from flask import render_template
import stochastic_sampling
from Tweet_Generator import markov, tokenize
import os
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


@app.route('/<int:num>')
def sentence_with_num_of_words(num):
    dirpath = os.getcwd()
    word_file = stochastic_sampling.process_histogram_without_numbers(
        dirpath+"/output.txt")

    sentence = stochastic_sampling.create_random_sentence(num, word_file)

    return render_template('index.html', sentence=sentence)


if __name__ == '__main__':
    app.run(debug=True)
