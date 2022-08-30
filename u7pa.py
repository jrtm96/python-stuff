# Given variables
alphabet = "abcdefghijklmnopqrstuvwxyz"

test_dups = ["zzz","dog","bookkeeper","subdermatoglyphic","subdermatoglyphics"]

test_miss = ["zzz","subdermatoglyphic","the quick brown fox jumps over the lazy dog"]

# Histogram function found in our textbook
def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


#Part 1
def has_duplicates(s):
    histo = histogram(s) # calling histogram function
    for a,b in histo.items(): # for loop the letters in the items
        if b > 1:
            return True  # If the String has any repeated characters it will return 'True'
        return False  #Otherwise it will return 'False'

for e in test_dups: # For each element in 'test_dups' list,
    if has_duplicates(e): # if the elements are duplicated
        print(e, ' has duplicates') # print element 'has duplicates'
    else:                            # otherwise,
        print(e, 'has no duplicates')  # print element 'has no duplicates'


#Part 2
def missing_letters(x): #function that displays the missing letters
    histo = histogram(x)
    y = [] #empty list
    for l in alphabet: # for letter in 'aplphabet'
        if l not in histo: #if letter not found in the histogram of the argument
            y.append(l) # append them
    return ''.join(y)  # otherwise return the empty list joined

for e in test_miss: # for each element in test_miss
    missl = missing_letters(e)  # call 'missing letters' function to see if
                                # letters are missing in elements and assign it to variable 'missl'
    if len(missl): # if the length of missl has missing letters
        print(e,'is missing letters', missl)  # print the element, 'is missing letters' and the letters missing
    else:                                      # otherwise,
        print(e,'uses all the letters')         # print the element and 'uses all the letters'

