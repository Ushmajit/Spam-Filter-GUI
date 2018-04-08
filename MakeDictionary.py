from collections import Counter
from FilterDictionary import filter_dictionary
import os


def makeDictionary(train_dir):
    emails = [os.path.join(train_dir, files) for files in os.listdir(train_dir)]
    all_words = []
    for mail in emails:
        with open(mail) as m:
            for i, line in enumerate(m):
                if i == 2:  # Body of email is only 3rd line of text file
                    words = line.split()
                    all_words += words
    #Start Filtering the alphanumeric words and the two letter words
    #all_words = filter_dictionary(all_words)
    dictionary = Counter(all_words)
    dictionary = dictionary.most_common(3000)
    return dictionary