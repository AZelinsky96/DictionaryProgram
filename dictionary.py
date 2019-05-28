#! /home/anthonyz/anaconda3/bin/python3
"""
Author: Anthony Zelinsky
Created 5/28/2019

Purpose:
To create an interactive dictionary to input words and retrieve definitions
"""


import json
import os






def loading_json():
    return json.load(open("data.json", "r"))



def adding_word(word):
    data = loading_json()
    data_insert = list()
    data_insert.append(str(input("Input definition of word {}: ".format(word))))
    data['{}'.format(word)] = data_insert
    with open("data.json", "w") as f:
        json.dump(data, f)

def finding_word():
    word = input("Please enter the word you wish to learn more about: ").lower()
    data = loading_json()
    try:
        data[word]
        return print("Word: {}\nDefinition: {}".format(word, data[word][0]))
    except:
        print("That word does not exist in the dictionary.")
        add_it = input("Would you like to add the word? [y/n]: ").lower()
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
