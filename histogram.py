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


def histogram_list_of_tuples(word_list):

    word_dict = {}

    for word in word_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    sorted_word_dict = sorted(word_dict.items(), key=itemgetter(1), reverse=True)

    return sorted_word_dict


def histogram_list_of_lists(word_list):

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
    new_word_list = []
    count_list = []

    for word in word_list:
        if word in new_word_list:
            word_index = new_word_list.index(word)
            new_word_list[word_index + 1] += 1
        else:
            new_word_list.append(word)
            new_word_list.append(0)

    for x in range(1, len(new_word_list), 2):
        if new_word_list[x] in count_list:
            count_index = count_list.index(new_word_list[x])
            count_word_list = count_list[count_index+1]
            word_list_index = count_list.index(count_word_list)
            # print(word_list_index)
            # print(word_index)
            count_list[word_list_index].append(new_word_list[x-1])
            # count_list.insert(x+1, [new_word_list[x-1]])
        else:
            count_list.append(new_word_list[x])
            count_list.append([new_word_list[x-1]])

    return count_list


def unique_words_count(word_list):
    return len(word_list)


def frequency(word, histogram):
    print([x[1] for x in histogram if x[0] == word])


# my_histogram = histogram_dict(file)

# histogram_list_of_count(file)
# my_histogram = histogram("/Users/Specialist/Desktop/TheScienceOfVocalPower.txt")
if __name__ == "__main__":
    file = process_file("/Users/Specialist/Desktop/GulliversTravels.txt")
    my_histogram = histogram_list_of_tuples(file)
    frequency('and', my_histogram)

    print(my_histogram)
    # histogram_list_of_lists(file)
    # file_to_write = open("/Users/Specialist/Documents/Code/Makeschool/CS-2_TweetGenerator/small_output.txt", "w")
    file_to_write = open("/Users/Specialist/Documents/Code/Makeschool/CS-2_TweetGenerator/output.txt", "w")
    for x in my_histogram:
        file_to_write.write(x[0] + " " + str(x[1]) + "\n")
