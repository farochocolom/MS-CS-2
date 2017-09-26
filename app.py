from flask import Flask
import stochastic_sampling
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, mundo!'

@app.route('/sentence')
def create_sentence():
    word_file = stochastic_sampling.process_histogram_without_numbers(
        "/Users/Specialist/Documents/Code/Makeschool/CS-2_TweetGenerator/output.txt")

    sentence = stochastic_sampling.create_random_sentence(10, word_file)
    return sentence