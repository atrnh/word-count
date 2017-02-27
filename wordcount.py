import string
import sys


def remove_punctuation(phrase):
    clean_phrase = [char for char in phrase if char not in string.punctuation]

    return ''.join(clean_phrase)

# remove_punctuation("Hello?,.")

def word_count():
    text_file = open(sys.argv[1])
    word_counts = {}

    for line in text_file:
        # get rid of trailing whitespace, get a list of words
        words = line.rstrip().split()

        for word in words:
            word = remove_punctuation(word)
            # update value or store a new key value pair
            word_counts[word.lower()] = word_counts.get(word.lower(), 0) + 1

    # get key value pairs from word_counts
    for word_key, word_value in word_counts.iteritems():
        # print key value pairs
        print word_key, word_value

    text_file.close()

word_count()

