from random import choice
from random import sample
import random
import time


def process_file(word_file):
    fh = open(word_file, "r")
    file = fh.read()
    wordList = file.split()
    return  wordList


def create_random_sentence(num, words):
    local_words = words
    final_word_list = []
    for word in range(0, num):
        rand_index = random.randint(0, len(local_words) - 1)
        final_word_list.append(local_words[rand_index])
        local_words.pop(rand_index)

    return " ".join(final_word_list)


def create_sentence(wordlist):
    print(" ".join(wordlist))


if __name__ == "__main__":
    process_file("/usr/share/dict/words")
    userIn = int(input("Enter a number: "))

    process_file()

    print(create_random_sentence(userIn))