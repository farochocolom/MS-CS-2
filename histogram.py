import random
import time
import re
from collections import Counter

def histogram(source_text):
    startTime = time.time()
    fh = open(source_text, "r")
    file = fh.read().lower()
    file = re.sub('[^a-z\ \']+', " ", file)
    wordList = file.split()

    word_dict = {}
    word_tuple_list = []

    for word in wordList:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    sorted_word_dict = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
    word_count = unique_words(sorted_word_dict)
    # counts = Counter(wordList)
    # elmax = counts.most_common(100)
    return sorted_word_dict


def unique_words(word_list):
    return len(word_list)



def frequency(word, histogram):
    word_dict = dict(histogram)
    print(word_dict[word])



# my_histogram = histogram("/Users/Specialist/Desktop/GulliversTravels.txt")
my_histogram = histogram("/Users/Specialist/Desktop/TheScienceOfVocalPower.txt")

frequency("you", my_histogram)