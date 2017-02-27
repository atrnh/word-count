def word_count(file_name):
    text_file = open(file_name)
    word_counts = {}

    for line in text_file:
        # split line by space, get rid of trailing white space
        words = line.rstrip().split()

        for word in words:
            word_counts[word] = word_counts.get(word, 0) + 1

    # loop over dictionary
    #     print key value pairs