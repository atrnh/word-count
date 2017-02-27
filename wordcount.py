def word_count(file_name):
    text_file = open(file_name)
    word_counts = {}

    for line in text_file:
        # get rid of trailing whitespace, get a list of words
        words = line.rstrip().split(' ')

        for word in words:
            # update value or store a new key value pair
            word_counts[word] = word_counts.get(word, 0) + 1

    # get key value pairs from word_counts
    for word_key, word_value in word_counts.iteritems():
        # print key value pairs
        print word_key, word_value

    text_file.close()

word_count("twain.txt")
