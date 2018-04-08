def filter_dictionary(words) :
      for item in words:
        if item.isalpha() == False:
            words.remove(item)
        elif len(item) == 1:
            words.remove(item)
      return words