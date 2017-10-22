import re
import sys


def clean_file(source_text):
    """Clean up a file """
    file_to_read = open(source_text, "r")
    read_file = file_to_read.read()

    read_file = re.sub("\n", " [STOP] ", read_file)
    read_file = re.sub('[^a-zA-Z’\.,\n]+', " ", read_file)
    read_file = re.sub('[\.]+', ". [STOP] ", read_file)
    # read_file = re.sub("([[STOP]  [STOP]])", " [STOP] ", read_file)

    read_file = re.sub("([\[STOP\] {2}\[STOP\]]+)\s", " [STOP] ", read_file)
    return read_file


if __name__ == '__main__':
    file = sys.argv[1]
    clean = clean_file(file)
    print(clean)
