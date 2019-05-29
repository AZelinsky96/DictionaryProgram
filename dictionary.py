## for ubuntu
#-! /home/anthonyz/anaconda3/bin/python3

# for mint
#!/home/zeski/anaconda3/bin/python3
 

"""
Author: Anthony Zelinsky
Created 5/28/2019

Purpose:
To create an interactive dictionary to input words and retrieve definitions
"""


import json
import os






def loading_json():
    """
    This is the function that will load the json into play.
    """
    return json.load(open("data.json", "r"))



def adding_word(word):
    """
    This function will be used to add the word to the data file with the input definition.
    """
    ## Loading the json in using function above
    data = loading_json()
    ## Creating a data insert list
    data_insert = list()
    ## Appending the values of the user input for word definition
    data_insert.append(str(input("Input definition of word {}: ".format(word))))
    ## Creating a new data entry for the input data above
    data['{}'.format(word)] = data_insert
    ## Appending the data to the data file
    with open("data.json", "w") as f:
        json.dump(data, f)

def finding_word():
    """
    This is the main function of the program. This will be used to input a word, and look it up within the data file.

    """
    ## Accepting user input
    word = input("Please enter the word you wish to learn more about: ").lower()
    ## Loading in the data file
    data = loading_json()

    try:
        ## This will print the word and associated definition
        data[word]
        return print("Word: {}\nDefinition: {}\n".format(word, data[word][0]))
    except:
        ## If the word is not located within the data file. It will inform user that it is not located within data file and ask to insert the word.
        print("That word does not exist in the dictionary.")
        ## Asking the user if they would like to add the word.
        add_it = input("Would you like to add the word? [y/n]: ").lower()
        ## Flow control for add it key
        if (add_it != "y") and (add_it != 'n'):
            while True:
                add_it = input("Error! Please Enter y or n")
                if (add_it == "y") or (add_it == "n"):
                    break
                else:
                    pass

        if add_it == "y":
            adding_word(word)
        elif add_it == "n":
            print("Word not added!")

def dictionary():
    while True:
        finding_word()

        ## Once the finding word function executes, it will ask to include another word. 
        break_word = input("Would you like to lookup another word? [y/n]").lower()

        if (break_word != "y") and (break_word != "n"):
            while True:
                break_word = input("Error: Please Enter y or n").lower()
                if (break_word == "y") or (break_word == "n"):
                    break
                else:
                    pass

        if break_word == "y":
            pass

        elif break_word == 'n':
            print("Great! Thank you.")
            break





def main():
    dictionary()


if __name__ == "__main__":
    main()
    print("\n\nThank you for using the dictionary! ")
