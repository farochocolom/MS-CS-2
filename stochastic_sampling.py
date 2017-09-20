import histogram
# import rearrange
# import dictionary_words
import sys
import re
import random
from operator import itemgetter

fh = open(sys.argv[1])
file = fh.read()
# file = re.sub('[^a-z\ \']+', " ", file)
# print(file)


def get_random_word(word_file):
    word_list = word_file.split()
    # print(word_list)
    # rand_index = random.randint(0, len(word_list) - 1)
    # print(word_list[rand_index])

@profile
def sampling(word_file, num):
    word_list = word_file.split()
    new_word_list = []
    sample_word_list = []

    word_dict = {}

    for x in range(0, len(word_list), 2):
        for y in range(int(word_list[x+1])):
            new_word_list.append((word_list[x]))

    # print(new_word_list)

    for x in range(0, num):
        rand_index = random.randint(0, len(new_word_list) - 1)
        sample_word_list.append(new_word_list[rand_index])

    # print(sample_word_list)


    for word in sample_word_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    # print(word_dict)

    sorted_word_dict = sorted(word_dict.items(), key=itemgetter(1), reverse=True)

    print(sorted_word_dict)
    # print(histogram.frequency())

sampling(file, 900000)

# histogram.histogram()