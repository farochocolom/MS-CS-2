import cleanup
import sys


def tokenize(source_text):
    read_file = cleanup.clean_file(source_text)
    word_list = read_file.split()
    return word_list


if __name__ == '__main__':
    file = sys.argv[1]
    clean = tokenize(file)
    print(clean)
