import collections
def commonChars(words):

    if len(words) < 2:
        return set(words[0])

    letters =  set(words[0])  #create a set from first word letter
    # print(letters)

    result = []

    for letter in letters:

        n_freq = min([word.count(letter) for word in words])  #get the freq of the letters of first
                                                            # word from the follwoing words and get min freq of this

        if n_freq>0:  #if the letter was repeated in following words

            result += [letter]*n_freq   #add it to o/p n_freq times

    return result


print(commonChars(["bella","label","hello"]))