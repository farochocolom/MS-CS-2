from flask import Flask
import stochastic_sampling
import os
app = Flask(__name__)

@app.route('/')
def hello_world():
    dirpath = os.getcwd()
    word_file = stochastic_sampling.process_histogram_without_numbers(
        dirpath+"/output.txt")

    sentence = stochastic_sampling.create_random_sentence(10, word_file)
    return sentence


if __name__ == '__main__':
    app.run()