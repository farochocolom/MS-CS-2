from pprint import pprint
from Tweet_Generator import tokenize, sample
from Tweet_Generator.histograms import Dictogram
from collections import ChainMap
import random


def markov_chain(words_list):
    word_dict = Dictogram()
    generated_histogram = Dictogram()
    for x in range(len(words_list)):
        current_word = words_list[x]

        if x + 1 < len(words_list):
            next_word = words_list[x + 1]
            generated_histogram.add(next_word)
            if current_word in word_dict:
                word_dict[current_word] = dict(ChainMap(word_dict[current_word], {next_word: generated_histogram[next_word]}))
            else:
                word_dict[current_word] = {next_word: generated_histogram[next_word]}
    return word_dict


def weighted_markov(markov_dict):
    for markov in markov_dict:
        histogram = markov_dict[markov]
        weighted_dicts = sample.create_weighted_sorted_tuple_list_markov(histogram)
        markov_dict[markov] = weighted_dicts

    return markov_dict


def walk_the_markov(num, weighted_markov_dict):
    sentence = []
    current_word = random.choice(list(weighted_markov_dict.keys()))
    for x in range(num):
        next_word = ""
        random_range = random.random()
        for item in weighted_markov_dict[current_word]:
            if random_range > float(item[0]):
                continue
            else:
                next_word = item[1]
        current_word = next_word
        sentence.append(next_word)

    return " ".join(sentence)


if __name__ == "__main__":
    fh = tokenize.tokenize('./../SoP.txt')
    markov_chain_var = markov_chain(fh)
    weighted = weighted_markov(markov_chain_var)
    walk_the_markov(10, weighted)
    # pprint(markov_chain_var)
