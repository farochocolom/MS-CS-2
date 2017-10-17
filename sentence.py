import random


def create_random_sentence(num, words):
    local_words = words
    final_word_list = []
    for _ in range(0, num):
        rand_index = random.randint(0, len(local_words) - 1)
        final_word_list.append(local_words[rand_index])
        local_words.pop(rand_index)

    return " ".join(final_word_list)
