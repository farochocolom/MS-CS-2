from random import choice
from random import sample
import random
import time


fh = open("/usr/share/dict/words","r")
file = fh.read()
sentence = ""
wordList = file.split()
print(wordList)
print(len(wordList))
print(sample(wordList, 5))


def best_preserve(num):
    startTime = time.time()
    process(sample(wordList, num))
    print(time.time() - startTime)


def process(wordlist):
    print(" ".join(wordlist))



best_preserve(int(input("Enter a number: ")))