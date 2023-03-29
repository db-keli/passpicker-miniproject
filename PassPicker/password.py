import random
import string
import pandas as pd

class Password:
        
    # A fuction that takes no arguments 
    # and prints our welcome message
    def welcome(self):
        print("\nWelcome to PassPicker\n\(*_*)/ \nI generate infinite random passwords.\nSecure your accounts!!\n")

    # Defining a function to return a random noun from
    # a file.
    def nounread(self):
        nouns = pd.read_csv("./PassPicker/english-nouns.csv")
        n = nouns.iloc[random.randrange(0,1525),0]
        n =str(n)
        return(n)

    # Defining a function to return a random adjective from
    # a file.  
    def adj_read(self):
        adjectives = pd.read_csv("./PassPicker/english-adjectives.csv")
        adj = adjectives.iloc[random.randrange(0,1347),0]
        adj = str(adj)
        return(adj)

    # Defining a function to generate a random number     
    def random_num(self):
        number = random.randrange(0,900)
        number = str(number)
        return(number)

    # Defining a function to generate a random character from 
    # the given list.
    def charread(self):
        char = random.choice(string.punctuation)
        char = str(char)
        return(char)
    
passcode = Password()