import histogram
# import rearrange
# import dictionary_words
import sys
import re
import random
from operator import itemgetter


def process_histogram_with_numbers(source_text):
    fh = open(source_text, "r")
    file = fh.read().lower()
    word_list = file.split()
    return word_list


def process_histogram_without_numbers(source_text):
    fh = open(source_text, "r")
    file = fh.read().lower()
    file = re.sub('[^a-z\']+', " ", file)
    word_list = file.split()
    return word_list


def get_random_word(word_file):
    rand_index = random.randint(0, len(word_file) - 1)

    return word_file[rand_index]


def get_random_word_with_weighted_dict(weighted_dict):
    rand_index = random.random()
    for weight in weighted_dict:
        if rand_index > float(weight[0]):
            continue
        else:
            return weight[1]


def get_total_word_count(word_list):
    total_words = 0
    for x in range(1, len(word_list), 2):
        total_words += int(word_list[x])

    return total_words


def create_list_with_weighting_range_from_word_list(word_list):
    list_with_weight_percentages = []
    list_with_weight_ranges = []
    total_words = get_total_word_count(word_list)
    weight_range = 0

    # for x in range(0,len(word_list), 2):
    #     word_percentage = int(word_list[x+1])/total_words
    #     list_with_weight_percentages.append([word_list[x], word_percentage])

    for x in range(0, len(word_list), 2):
        word_percentage = int(word_list[x + 1]) / total_words
        weight_range += word_percentage
        list_with_weight_percentages.append([word_list[x], weight_range])

    return list_with_weight_percentages


def create_dict_with_weighting_range_from_word_list(word_list):
    dict_with_weight_percentages = {}
    total_words = get_total_word_count(word_list)
    weight_range = 0

    # for x in range(0,len(word_list), 2):
    #     word_percentage = int(word_list[x+1])/total_words
    #     list_with_weight_percentages.append([word_list[x], word_percentage])

    for x in range(0, len(word_list), 2):
        word_percentage = int(word_list[x + 1]) / total_words
        weight_range += word_percentage
        dict_with_weight_percentages[weight_range] = word_list[x]

    sorted_word_dict = sorted(dict_with_weight_percentages.items(), key=itemgetter(0))
    return sorted_word_dict


def sample(num, word_file):

    word_list = []

    for _ in range(num):
        rand_word = get_random_word_with_weighted_dict(word_file)
        word_list.append(rand_word)

    return histogram.histogram_dict(word_list)



test_histogram = process_histogram_with_numbers("/Users/Specialist/Documents/Code/Makeschool/CS-2_TweetGenerator/small_word_file.txt")
# create_list_with_weighting_range_from_word_list(histogram)
weighting_sample = create_dict_with_weighting_range_from_word_list(test_histogram)
print(weighting_sample)

print(sample(100000, weighting_sample))