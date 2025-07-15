#!/usr/bin/env python3

# This script takes a length of text and searches it to see if a given word 
# exists within that string. The letters of ther word to find must appear in order,
# but the letters do not have to be consecutive.



def clean_words(test_case, word_to_find):
        test_case = test_case.replace(' ', '').lower()
        word_to_find = word_to_find.replace(' ', '').lower()
        if not word_to_find.isalpha():
            print('The given input contains invalid characters.')
        else:
            find_word(test_case, word_to_find)


def find_word(test_case, word_to_find):
    index = 0
    valid = True
    for i in range(len(word_to_find)):
         index = test_case.find(word_to_find[i], index) + 1
         if index == 0:
              valid = False
              break
    if valid:
         print('Yes! The word does exist!')
    else:
         print('Oh, sorry. That word does not appear in the text.')



if __name__ == '__main__':
    test_case = 'vcxzxduGDGDAGRybfdsobywuefgas'
    word_to_find = 'dog'
    clean_words(test_case, word_to_find)  
