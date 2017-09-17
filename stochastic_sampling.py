import histogram
# import rearrange
# import dictionary_words
import sys
import re
import random

fh = open(sys.argv[1])
file = fh.read()
file = re.sub('[^a-z\ \']+', " ", file)
# print(file)


def get_random_word(word_file):
    word_list = word_file.split()
    # print(word_list)
    rand_index = random.randint(0, len(word_list) - 1)
    print(word_list[rand_index])

get_random_word(file)
# histogram.histogram()