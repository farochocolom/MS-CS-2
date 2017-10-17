import re
import sys


def clean_file(source_text):
    """Clean up a file """
    file_to_read = open(source_text, "r")
    read_file = file_to_read.read()
    read_file = re.sub('[^a-zA-Z’]+', " ", read_file)
    # ([a - zA - Z'-]+).(\S*[’[a-z])
    return read_file


if __name__ == '__main__':
    file = sys.argv[1]
    clean = clean_file(file)
    print(clean)
