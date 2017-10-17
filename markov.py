from pprint import pprint
import tokenize_corpus
import sample
from histograms import Dictogram
import linkedList
import hash_table
# from hash_table import HashTable
# from queue import Queue
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
                word_dict[current_word] = dict(
                        ChainMap(word_dict[current_word],
                        {next_word: generated_histogram[next_word]})
                    )
            else:
                word_dict[current_word] = {next_word: generated_histogram[next_word]}
    return word_dict


def markov_chain_2nd_order(words_list):
    window = linkedList.LinkedList()
    word_dict = Dictogram()
    start_list = []
    generated_histogram = Dictogram()
    for word in words_list:

        if window.length() == 2:
            start_list.append((window.head.data, window.head.next.data))

        if window.length() == 3:

            current_key = window.head.data, window.head.next.data
            next_word = window.head.next.next.data
            window.dequeue().data
            generated_histogram.add(next_word)
            if next_word == "[STOP]" and current_key in word_dict:

                word_dict[current_key] = dict(
                        ChainMap(word_dict[current_key],
                        {next_word: generated_histogram[next_word]})
                    )
                window = linkedList.LinkedList()

            elif current_key in word_dict:
                word_dict[current_key] = dict(
                        ChainMap(word_dict[current_key],
                        {next_word: generated_histogram[next_word]})
                    )
            else:
                word_dict[current_key] = {next_word: generated_histogram[next_word]}

        window.enqueue(word)
        word_dict["START"] = start_list

    return word_dict


def weighted_markov(markov_dict):
    for markov in markov_dict:
        if markov != "START":
            histogram = markov_dict[markov]
            weighted_dicts = sample.create_weighted_sorted_tuple_list_markov(histogram)
            markov_dict[markov] = weighted_dicts

    return markov_dict


def walk_the_markov(weighted_markov_dict):
    sentence = []
    current_word = random.choice(list(weighted_markov_dict["START"]))
    sentence.append(current_word[0])
    sentence.append(current_word[1])

    next_word = ""
    random_range = random.random()
    for item in weighted_markov_dict[current_word]:
        if random_range > float(item[0]):
            continue
        else:
            next_word = (current_word[1], item[1])

        if next_word == "[STOP]":
            break

    current_word = next_word
    sentence.append(next_word[1])

    return " ".join(sentence)


if __name__ == "__main__":
    fh = tokenize_corpus.tokenize('./corpus.txt')
    markov_chain_var = markov_chain_2nd_order(fh)

    weighted = weighted_markov(markov_chain_var)
    # pprint(weighted)
    sentence = walk_the_markov(weighted)
    print(sentence)
