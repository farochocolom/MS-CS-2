from pprint import pprint
from Tweet_Generator import tokenize
from Tweet_Generator.histograms import Dictogram
from collections import ChainMap

fh = tokenize.tokenize('./../SoP.txt')
print(fh)

# gen_list = Dictogram(fh)
# print(gen_list)
#
def generate_word_list(words_list):
    follow_list = []
    for x in range(len(words_list)):
        if x + 1 < len(words_list):
            follow_list.append(words_list[x+1])

    return follow_list


def markov_chain(words_list):
    word_dict = {}
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
    # print(generated_histogram.tokens)
    # print(generated_histogram.types)
    return word_dict

#
pprint(markov_chain(fh))
