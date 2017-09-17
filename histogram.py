import random
import time
import re
from collections import Counter
from operator import itemgetter


def histogram(source_text):
    start_time = time.time()
    fh = open(source_text, "r")
    file = fh.read().lower()
    file = re.sub('[^a-z\ \']+', " ", file)
    word_list = file.split()

    word_dict = {}
    # word_dict = {word: 1 if word in word_list else value+1 for word, value in word_list}
    # word_tuple_list = []

    for word in word_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1


    # sorted_word_dict = sorted(word_dict.items(), key=lambda word_tuple: word_tuple[1], reverse=True)
    sorted_word_dict = sorted(word_dict.items(), key=itemgetter(1), reverse=True)
    # counts = Counter(wordList)
    # elmax = counts.most_common(100)

    print(time.time() - start_time)

    print(sorted_word_dict)
    return sorted_word_dict


def unique_words(word_list):
    return len(word_list)


def frequency(word, histogram):
    start_time = time.time()
    print([x[1] for x in histogram if x[0] == word])
    print(time.time() - start_time)
    # word_dict = dict(histogram)
    # print(word_dict[word])


my_histogram = histogram("/Users/Specialist/Desktop/GulliversTravels.txt")
# my_histogram = histogram("/Users/Specialist/Desktop/TheScienceOfVocalPower.txt")

frequency("the", my_histogram)