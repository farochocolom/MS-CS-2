import random
import time
import re
from collections import Counter




def histogram(source_text):
    fh = open(source_text, "r")
    file = fh.read().lower()
    file = re.sub('[^a-z\ \']+', " ", file)
    # print(file)
    wordList = file.split()
    # print(len(wordList))
    # print(wordList)

    word_dict = {}
    word_tuple_list = []

    for word in wordList:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    sorted_word_dict = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
    word_count = unique_words(sorted_word_dict)
    print(word_count)
    # print(word_dict)
    # print(sorted_word_dict)
    # print(word_tuple_list)
    # counts = Counter(wordList)
    # elmax = counts.most_common(100)
    # print(elmax)
    print(sorted_word_dict)
    return sorted_word_dict


def unique_words(word_list):
    return len(word_list)


histogram("/Users/Specialist/Desktop/GulliversTravels.txt")

# import re, time
# from collections import Counter
#
# startTime = time.time()
# file = open('/Users/Specialist/Downloads/Ulysses_NT.txt', 'r')
#
# text = file.read().lower()
# file.close()
#
# text = re.sub('[^a-z\ \']+', " ", text)
# words = list(text.split())
#
# counts = Counter(words)
# elmax = counts.most_common(100)
# print(elmax)
# print(time.time() - startTime)