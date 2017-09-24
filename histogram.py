import random
import time
import re
from collections import Counter
from operator import itemgetter


def process_file(source_text):
    fh = open(source_text, "r")
    file = fh.read().lower()
    file = re.sub('[^a-z\']+', " ", file)
    word_list = file.split()
    return word_list

def histogram_dict(word_list):

    word_dict = {}

    for word in word_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1


    return word_dict


def histogram_list_of_lists(word_list):

    new_word_list = []
    list_of_lists = []

    for word in word_list:
        if word in new_word_list:
            word_index = new_word_list.index(word)
            new_word_list[word_index + 1] += 1
        else:
            new_word_list.append(word)
            new_word_list.append(0)

    for x in range(0, len(new_word_list), 2):
        list_of_lists.append([new_word_list[x], new_word_list[x+1]])

    print(list_of_lists)


def unique_words(word_list):
    return len(word_list)


def frequency(word, histogram):
    # start_time = time.time()
    print([x[1] for x in histogram if x[0] == word])
    # print(time.time() - start_time)
    # word_dict = dict(histogram)
    # print(word_dict[word])

file = process_file("/Users/Specialist/Desktop/GulliversTravels.txt")

# my_histogram = histogram_dict(file)
histogram_list_of_lists(file)
# my_histogram = histogram("/Users/Specialist/Desktop/TheScienceOfVocalPower.txt")
# if __name__ == "__main__":
#     frequency("the", my_histogram)
#
#     # file_to_write = open("/Users/Specialist/Documents/Code/Makeschool/CS-2_TweetGenerator/small_output.txt", "w")
#     file_to_write = open("/Users/Specialist/Documents/Code/Makeschool/CS-2_TweetGenerator/output.txt", "w")
#     for x in my_histogram:
#         file_to_write.write(x[0] + " " + str(x[1]) + "\n")
