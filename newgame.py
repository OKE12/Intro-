
easystring = '''


A ___1___ is created with the def keyword. You specify the inputs a ___2___ takes by
adding ___3___ separated by commas between the parentheses. ___4___s by default return ___5___ if you don't specify the value to return. ___6___ can be standard data types such as string, number, dictionary, tuple, and ___7___ or can be more complicated such as objects and lambda functions.'''

answers_easy = ["___1___","___2___","___4___","___3___","___5___","___6___","___7___"]


def word_in_pos(word, parts_of_speech):
    for pos in parts_of_speech:
        if pos in word:
            return pos
    return None




def play_game(ml_string, parts_of_speech):
    replaced = []
    ml_string = ml_string.split()
    for word in ml_string:
        replacement = word_in_pos(word, parts_of_speech)
        if replacement != None:
            user_input = raw_input('''

Eenter answer to number ''' + replacement + " here:")
            count = 0
            blanks_index = 0
            if user_input == answers[count]:



                word = word.replace(replacement, user_input)
                replaced.append(word)
                ml_string = "".join(ml_string)
                replaced_string = ml_string.replace(answers [blanks_index], user_input.upper())
                print replaced_string
                blanks_index += 1
                count += 1


                print replaced_string
            else:
                return "wrong answer"
                replaced.append(word)
    replaced = " ".join(replaced)
    return replaced


print "Hello and welcome to my game."
selectlevel = raw_input('''
please select the level of difficulty by typing easy, medium. or hard:''')
if selectlevel == "easy":
    answers =  ["function", "fuction", "arguments", "arguments", "None","arguments", "lists"]
    print easystring
    print play_game(easystring, answers_easy)
