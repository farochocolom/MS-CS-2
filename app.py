from flask import Flask
import stochastic_sampling
app = Flask(__name__)

@app.route('/')
def hello_world():
    word_file = stochastic_sampling.process_histogram_without_numbers(
        "/Users/Specialist/Documents/Code/Makeschool/CS-2_TweetGenerator/output.txt")

    sentence = stochastic_sampling.create_random_sentence(10, word_file)
    return sentence


if __name__ == '__main__':
    app.run()