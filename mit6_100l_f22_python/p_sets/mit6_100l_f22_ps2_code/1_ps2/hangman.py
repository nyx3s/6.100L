# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for char in secret_word:
        if char not in letters_guessed:
            return False
    return True


def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    re = ""
    for char in secret_word:
        if char not in letters_guessed:
            re += "*"
        else:
            re += char
    return re


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters = list("abcdefghijklmnopqrstuvwxyz")
    
    for char in letters_guessed:
        if char in letters:
            letters.remove(char)
    
    return ''.join(letters)


def get_reveal(secret, avall):
    """
    @pram secret is string word that is secret
    avall list of avalibe letter in the crrunt game
    @return charcter that is random form the secret
    """
    a = [i for i in avall if i in secret]
    rand = random.randint(0,len(a)-1)
    return a[rand]

def hangman(secret_word, with_help):
    """
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '!'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol !, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    num_of_guess = 10
    length = len(secret_word)
    
    print("welcome to hangman ")
    print(f"iam thinking of word has length of {length}")
    print("______s__t__a__r__t______")
    #print("note u shold inter one letter at time or <!> of u want help that well cost u 
          #/n 3 guess and revel one letter ")
    
    l = []
    good_letter = list("abcdefghigklmnopqrstuvwxyz!")
    vol = list("aeuio")
    while num_of_guess > 0:
        
        print(f"u have {num_of_guess}")
        
        aval = get_available_letters(l)
        print(f"avalible letters so far {aval}")
        
        guess = input("inter u gess >> ").lower()
        
        l.append(guess)

        prog = get_word_progress(secret_word, l)

        if guess == '!' and with_help:
            if num_of_guess > 3:

                revel_letter = get_reveal(secret_word, aval)
                print(f"letter reveled <{revel_letter}>")

                l.append(revel_letter)
                print(f"look {get_word_progress(secret_word, l)}")

                num_of_guess -= 3
            else:
                input("not enuogh gaz press inter to return ")

        elif guess in secret_word and guess in aval and guess != "":
            print(f"good guess {prog}")

        elif guess not in good_letter:
            print("oppss plese inter a valed single char from above ")

        elif guess not in aval:
            print(f"u already guessd that letter <{guess}>")

        else:
            if guess in vol:
                num_of_guess -=1

            print(f"obss wrong {prog}")
            num_of_guess -= 1

        print("________________________________")

        if has_player_won(secret_word, l):

            score = ((num_of_guess + 4) * get_unigh(secret_word)) + (3 * length)
            print(f"congrtes u won score: {score}")
            break

        elif num_of_guess < 1:
            print(f"sorry u run out of guess the word was {secret_word}")
            break




def get_unigh(s):
    a = []
    for i in s:
        if i not in a:
            a.append(i)
    return len(a)

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test


if __name__ == "__main__":
    # To test your game, uncomment the following three lines.

    secret_word = "is"#choose_word(wordlist)
    with_help = True
    hangman(secret_word, with_help)

    # After you complete with_help functionality, change with_help to True
    # and try entering "!" as a guess!

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run ps2_student_tester.py
    # one more time before submitting to make sure all the tests pass.
    pass

