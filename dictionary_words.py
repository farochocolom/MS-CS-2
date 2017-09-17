from random import choice
from random import sample
import random
import time


fh = open("/usr/share/dict/words","r")
file = fh.read()
sentence = ""
wordList = file.split()
# print(wordList)
# print(len(wordList))
# print(sample(wordList, 5))


def create_random_sentence(num, words=wordList):
    startTime = time.time()

    localWords = words
    finalWordList = []
    for word in range(0, num):
        rand_index = random.randint(0, len(localWords) - 1)
        finalWordList.append(localWords[rand_index])
        localWords.pop(rand_index)

    print(time.time() - startTime)
    return " ".join(finalWordList)




def process(wordlist):
    print(" ".join(wordlist))

userIn = int(input("Enter a number: "))

print(create_random_sentence(userIn))