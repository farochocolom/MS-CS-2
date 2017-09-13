import random
import sys

wordList = sys.argv
del wordList[0]
random.shuffle(wordList)
sentence = " ".join(wordList)
print(sentence)

# def random_python_quote():
#     rand_index = random.randint(0, len(quotes) - 1)
#     return quotes[rand_index]
#
# if __name__ == '__main__':
#     quote = random_python_quote()
#     print quote
