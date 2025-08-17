# 6.100A Fall 2022
# Problem Set 3
# Written by: sylvant, muneezap, charz, anabell, nhung, wang19k, asinelni, shahul, jcsands

# Problem Set 3
# Name:
# Collaborators:

# Purpose: Check for similarity between two texts by comparing different kinds of word statistics.

import string
import math


### DO NOT MODIFY THIS FUNCTION
def load_file(filename):
    """
    Args:
        filename: string, name of file to read
    Returns:
        string, contains file contents
    """
    # print("Loading file %s" % filename)
    inFile = open(filename, 'r')
    line = inFile.read().strip()
    for char in string.punctuation:
        line = line.replace(char, "")
    inFile.close()
    return line.lower()


### Problem 0: Prep Data ###
def text_to_list(input_text):
    """
    Args:
        input_text: string representation of text from file.
                    assume the string is made of lowercase characters
    Returns:
        list representation of input_text, where each word is a different element in the list
    """
    return input_text.split()


### Problem 1: Get Frequency ###
def get_frequencies(input_iterable):
    """
    Args:
        input_iterable: a string or a list of strings, all are made of lowercase characters
    Returns:
        dictionary that maps string:int where each string
        is a letter or word in input_iterable and the corresponding int
        is the frequency of the letter or word in input_iterable
    Note: 
        You can assume that the only kinds of white space in the text documents we provide will be new lines or space(s) between words (i.e. there are no tabs)
    """
    re = {}
    for item in input_iterable:

        if item not in re:
            re[item] = 1
        else:
            re[item] += 1
    return re


### Problem 2: Letter Frequencies ###
def get_letter_frequencies(word):
    """
    Args:
        word: word as a string
    Returns:
        dictionary that maps string:int where each string
        is a letter in word and the corresponding int
        is the frequency of the letter in word
    """
    return  get_frequencies(word)


def dic_to_set(dic1,dic2):
    """ dic1 and dic2 are dictenary of word and values
        how many word in that dict
        return a set of uniqe word in both of tow """
    l1 = set(dic1.keys())
    l2 = set(dic2.keys())
    l1.update(l2)
    #print(l1)
    #input()
    return l1


def num_of_word_in_files(list_files,word):
    """ list_files : list of file name paths to load
        word : string word to search for
        return number of appernce of that word in hole
        list of file names """
    
    count = 0
    for file in list_files:

        stringFile = load_file(file)
        list_of_word = text_to_list(stringFile)
        dic_freq = get_frequencies(list_of_word)
        if word in dic_freq:
            count +=1
    return count


### Problem 3: Similarity ###
def calculate_similarity_score(freq_dict1, freq_dict2):
    """
    The keys of dict1 and dict2 are all lowercase,
    you will NOT need to worry about case sensitivity.

    Args:
        freq_dict1: frequency dictionary of letters of word1 or words of text1
        freq_dict2: frequency dictionary of letters of word2 or words of text2
    Returns:
        float, a number between 0 and 1, inclusive
        representing how similar the words/texts are to each other

        The difference in words/text frequencies = DIFF sums words
        from these three scenarios:
        * If an element occurs in dict1 and dict2 then
          get the difference in frequencies
        * If an element occurs only in dict1 then take the
          frequency from dict1
        * If an element occurs only in dict2 then take the
          frequency from dict2
         The total frequencies = ALL is calculated by summing
         all frequencies in both dict1 and dict2.
        Return 1-(DIFF/ALL) rounded to 2 decimal places
    """
    diff, total = (0,0)
    items = dic_to_set(freq_dict1,freq_dict2)

    for item in items:
       
        if item in freq_dict1 and item in freq_dict2:
            diff += abs(freq_dict1[item] - freq_dict2[item])
            total += freq_dict1[item] + freq_dict2[item]

        elif item in freq_dict1 and item not in freq_dict2 :
            diff += freq_dict1[item]
            total += freq_dict1[item]
        else:
            diff += freq_dict2[item]
            total += freq_dict2[item]
        #print(diff,total,item,freq_dict1,freq_dict2) 
        #input("?? ")
    return round(1 - (diff/total), 2)


### Problem 4: Most Frequent Word(s) ###
def get_most_frequent_words(freq_dict1, freq_dict2):
    """
    The keys of dict1 and dict2 are all lowercase,
    you will NOT need to worry about case sensitivity.

    Args:
        freq_dict1: frequency dictionary for one text
        freq_dict2: frequency dictionary for another text
    Returns:
        list of the most frequent word(s) in the input dictionaries

    The most frequent word:
        * is based on the combined word frequencies across both dictionaries.
          If a word occurs in both dictionaries, consider the sum the
          freqencies as the combined word frequency.
        * need not be in both dictionaries, i.e it can be exclusively in
          dict1, dict2, or shared by dict1 and dict2.
    If multiple words are tied (i.e. share the same highest frequency),
    return an alphabetically ordered list of all these words.
    """
     # Combine the word frequencies from both dictionaries
    combined_freq = {}

    for word, freq in freq_dict1.items():
        combined_freq[word] = freq
    
    for word, freq in freq_dict2.items():
        if word in combined_freq:
            combined_freq[word] += freq
        else:
            combined_freq[word] = freq

    # Find the maximum frequency
    max_freq = max(combined_freq.values())

    # Collect all words with the maximum frequency
    most_frequent = [word for word, freq in combined_freq.items() if freq == max_freq]

    # Return the list sorted alphabetically
    return sorted(most_frequent)


### Problem 5: Finding TF-IDF ###
def get_tf(file_path):
    """
    Args:
        file_path: name of file in the form of a string
    Returns:
        a dictionary mapping each word to its TF

    * TF is calculatd as TF(i) = (number times word *i* appears
        in the document) / (total number of words in the document)
    * Think about how we can use get_frequencies from earlier
    """
    stringFile = load_file(file_path)
    list_of_word = text_to_list(stringFile)
    dic_freq = get_frequencies(list_of_word)
    tf_dic = {}
    
    for word,freq in dic_freq.items():
        #print(word,freq)
        #input()
        tf_dic[word] = (freq / len(list_of_word))
    
    return tf_dic


def get_idf(file_paths):
    """
    Args:
        file_paths: list of names of files, where each file name is a string
    Returns:
       a dictionary mapping each word to its IDF

    * IDF is calculated as IDF(i) = log_10(total number of documents / number of
    documents with word *i* in it), where log_10 is log base 10 and can be called
    with math.log10()

    """

    idf_dic = {}
    for file in file_paths:

        stringFile = load_file(file)
        list_of_word = text_to_list(stringFile)
        dic_freq = get_frequencies(list_of_word)

        for word in dic_freq:
            log_score = math.log10(len(file_paths) / num_of_word_in_files(file_paths,word))
            idf_dic[word] = log_score
    
    return idf_dic


def get_tfidf(tf_file_path, idf_file_paths):
    """
        Args:
            tf_file_path: name of file in the form of a string (used to calculate TF)
            idf_file_paths: list of names of files, where each file name is a string
            (used to calculate IDF)
        Returns:
           a sorted list of tuples (in increasing TF-IDF score), where each tuple is
           of the form (word, TF-IDF). In case of words with the same TF-IDF, the
           words should be sorted in increasing alphabetical order.

        * TF-IDF(i) = TF(i) * IDF(i)
        """
    tf_dic = get_tf(tf_file_path)
    idf_dic = get_idf(idf_file_paths)
    output = []
    for word,tf in tf_dic.items():

        output.append((word,(tf * idf_dic[word]),))

    return output


if __name__ == "__main__":
    pass
    ###############################################################
    ## Uncomment the following lines to test your implementation ##
    ###############################################################

    ## Tests Problem 0: Prep Data
    # test_directory = "tests/student_tests/"
    # hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
    # world, friend = text_to_list(hello_world), text_to_list(hello_friend)
    # print(world)      # should print ['hello', 'world', 'hello']
    # print(friend)     # should print ['hello', 'friends']

    ## Tests Problem 1: Get Frequencies
    # test_directory = "tests/student_tests/"
    # hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
    # world, friend = text_to_list(hello_world), text_to_list(hello_friend)
    # world_word_freq = get_frequencies(world)
    # friend_word_freq = get_frequencies(friend)
    # print(world_word_freq)    # should print {'hello': 2, 'world': 1}
    # print(friend_word_freq)   # should print {'hello': 1, 'friends': 1}

    ## Tests Problem 2: Get Letter Frequencies
    # freq1 = get_letter_frequencies('hello')
    # freq2 = get_letter_frequencies('that')
    # print(freq1)      #  should print {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    # print(freq2)      #  should print {'t': 2, 'h': 1, 'a': 1}

    ## Tests Problem 3: Similarity
    #test_directory = "tests/student_tests/"
    #hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
    #world, friend = text_to_list(hello_world), text_to_list(hello_friend)
    #world_word_freq = get_frequencies(world)
    #friend_word_freq = get_frequencies(friend)
    #word1_freq = get_letter_frequencies('toes')
    #word2_freq = get_letter_frequencies('that')
    #word3_freq = get_frequencies('nah')
    #word_similarity1 = calculate_similarity_score(word1_freq, word1_freq)
    #word_similarity2 = calculate_similarity_score(word1_freq, word2_freq)
    #word_similarity3 = calculate_similarity_score(word1_freq, word3_freq)
    #word_similarity4 = calculate_similarity_score(world_word_freq, friend_word_freq)
    #print(word_similarity1)       # should print 1.0
    #print(word_similarity2)       # should print 0.25
    #print(word_similarity3)       # should print 0.0
    #print(word_similarity4)       # should print 0.4

    ## Tests Problem 4: Most Frequent Word(s)
    # freq_dict1, freq_dict2 = {"hello": 5, "world": 1}, {"hello": 1, "world": 5}
    # most_frequent = get_most_frequent_words(freq_dict1, freq_dict2)
    # print(most_frequent)      # should print ["hello", "world"]

    ## Tests Problem 5: Find TF-IDF
    tf_text_file = 'tests/student_tests/hello_world.txt'
    idf_text_files = ['tests/student_tests/hello_world.txt', 'tests/student_tests/hello_friends.txt']
    tf = get_tf(tf_text_file)
    idf = get_idf(idf_text_files)
    tf_idf = get_tfidf(tf_text_file, idf_text_files)
    print(tf)     # should print {'hello': 0.6666666666666666, 'world': 0.3333333333333333}
    print(idf)    # should print {'hello': 0.0, 'world': 0.3010299956639812, 'friends': 0.3010299956639812}
    print(tf_idf) # should print [('hello', 0.0), ('world', 0.10034333188799373)]
