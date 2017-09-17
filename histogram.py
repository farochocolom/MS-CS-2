import random
import time
import re

def histogram(source_text):
    fh = open(source_text, "r")
    file = fh.read()
    sentence = ""
    wordList = file.split()
    print(wordList)


histogram("/Users/Specialist/Desktop/TheScienceOfVocalPower.txt")