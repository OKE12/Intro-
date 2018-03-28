# A list of replacement words to be passed in to the play game function.


# The following are some test strings to pass in to the play_game function.
easystring = '''


A ___1___ is created with the def keyword. You specify the inputs a ___2___ takes by
adding ___3___ separated by commas between the parentheses. ___4___s by default return ___5___ if you don't specify the value to return. ___6___ can be standard data types such as string, number, dictionary, tuple, and ___7___ or can be more complicated such as objects and lambda functions.'''

answers_easy = ["___1___","___2___","___4___","___3___","___5___","___6___","___7___"]



# Checks if a word in parts_of_speech is a substring of the word passed in.
def word_in_pos(word, parts_of_speech):
    for pos in parts_of_speech:
        if pos in word:
            return pos
    return None

# Plays a full game of mad_libs. A player is prompted to replace words in ml_string,
# which appear in parts_of_speech with their own words.


def play_game(ml_string, parts_of_speech):
    replaced = []
    ml_string = ml_string.split()
    for word in ml_string:
        replacement = word_in_pos(word, parts_of_speech)
        if replacement != None:
            user_input = raw_input('''

Eenter anser to number ''' + replacement + " here:")

            word = word.replace(replacement, user_input)
            replaced.append(word)
        else:
            replaced.append(word)
    replaced = " ".join(replaced)
    return replaced


print "Hello and welcome to my game."
selectlevel = raw_input('''

please select the level of difficulty by typing easy, medium. or hard:''')
if selectlevel == "easy":
    print easystring
    print play_game(easystring, answers_easy)



#I think they want us to fill in our own items for ml_string, and to put another part of speech.
