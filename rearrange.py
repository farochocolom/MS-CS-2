# -*- coding: utf-8 -*-
import random
import sys
import time

wordList = sys.argv
del wordList[0]
print(wordList[2])
# print(wordList[::-1])
# random.shuffle(wordList)
sentence = " ".join(wordList)
print(sentence)

def random_python_quote(words):
    startTime = time.time()
    localWords = words
    finalWordList = []
    for word in range(0, len(words)):
        rand_index = random.randint(0, len(localWords) - 1)
        finalWordList.append(localWords.pop(rand_index))
    print(time.time() - startTime)
    return " ".join(finalWordList)


print(random_python_quote(wordList))

# TODO
# String reversals: reverse words, sentences

# a[start:end]      # items start through end-1
# a[start:]         # items start through the rest of the array
# a[:end]           # items from the beginning through end-1
# a[:]              # a copy of the whole array
# a[start:end:step] # start through not past end, by step

# That's the same as a[:] a copy of the whole list, with a :step value of -1,
# which results in a reversed copy of the whole list
# print(sentence[::-1])
# print(reversed(sentence))
# print(list(reversed(sentence)))
# print(str(reversed(sentence)))
#
# print(''.join(reversed(sentence)))

# An interactive "mad libs" script

#
# number = input("Number: ")
# profession1 = input("Enter a profession: ")
# profession2 = input("Enter another profession: ")
# city1 = input("Enter a city: ")
# name = input("Enter a name: ")
# city2 = input("Enter another city: ")
# profession3 = input("Enter another profession: ")
# bodypart = input("Enter a body part: ")
#
# print(number + " years after the end of Rush Hour 2, James Carter is no longer a " + profession1 + ", but a " + profession2 + " on the streets of " + city1 + ". Lee is now the bodyguard for his friend " + name + ". Lee is still upset with Carter about an incident in " + city2 + " when Carter accidentally shot Lee`s girlfriend, " + profession3 + "Isabella Molina, in the " + bodypart + ".")

# Anagram generator
