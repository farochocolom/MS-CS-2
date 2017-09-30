import re
from operator import itemgetter


def process_file(source_text):
    file_to_read = open(source_text, "r")
    read_file = file_to_read.read().lower()
    read_file = re.sub('[^a-z\']+', " ", read_file)
    word_list = read_file.split()
    return word_list


def histogram_dict(word_list):

    word_dict = {}

    for word in word_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    return word_dict


def create_tuplegram(word_list):
    """Create a histogram composed of a list of tuples"""
    word_dict = {}

    for word in word_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    sorted_word_dict = sorted(word_dict.items(), key=itemgetter(1), reverse=True)

    return sorted_word_dict


def create_listogram(word_list):
    """Create a histogram composed of a list of lists"""
    new_word_list = []
    list_of_lists = []

    for word in word_list:
        if word in new_word_list:
            word_index = new_word_list.index(word)
            new_word_list[word_index + 1] += 1
        else:
            new_word_list.append(word)
            new_word_list.append(0)

    for x in range(0, len(new_word_list), 2):
        list_of_lists.append([new_word_list[x], new_word_list[x+1]])

    return list_of_lists


def histogram_list_of_count(word_list):
    """Create a histogram composed of a list of counts"""
    new_word_list = []
    count_list = []

    for word in word_list:
        if word in new_word_list:
            word_index = new_word_list.index(word)
            new_word_list[word_index + 1] += 1
        else:
            new_word_list.append(word)
            new_word_list.append(0)

    for current_index in range(1, len(new_word_list), 2):
        if new_word_list[current_index] in count_list:
            count_index = count_list.index(new_word_list[current_index])
            count_word_list = count_list[count_index+1]
            word_list_index = count_list.index(count_word_list)
            count_list[word_list_index].append(new_word_list[current_index-1])
        else:
            count_list.append(new_word_list[current_index])
            count_list.append([new_word_list[current_index-1]])

    return count_list


def unique_words_count(word_list):
    return len(word_list)


def frequency(word, histogram):
    print([x[1] for x in histogram if x[0] == word])


if __name__ == "__main__":
    # file = process_file("/Users/Specialist/Desktop/TheScienceOfVocalPower.txt")
    file = process_file("/Users/Specialist/Desktop/GulliversTravels.txt")
    my_histogram = create_tuplegram(file)
    frequency('and', my_histogram)

    # histogram_list_of_lists(file)
    # file_to_write = open("/Users/Specialist/Documents/Code/Makeschool/CS-2_TweetGenerator/small_output.txt", "w")
    file_to_write = open("/Users/Specialist/Documents/Code/Makeschool/CS-2_TweetGenerator/output.txt", "w")
    for x in my_histogram:
        file_to_write.write(x[0] + " " + str(x[1]) + "\n")
