import random
import string
import pandas as pd


# A fuction that takes no arguments 
# and prints our welcome message
def Welcome():
    print("\nWelcome to PassPicker\n\(*_*)/ \nI generate infinite random passwords.\nSecure your accounts!!\n")

# Defining a function to return a random noun from
# a file.
def nounread():
    nouns = pd.read_csv("/home/kekeli/Desktop/PyProjects/PassPicker/english-nouns.csv")
    n = nouns.iloc[random.randrange(0,1525),0]
    n =str(n)
    return(n)

# Defining a function to return a random adjective from
# a file.  
def adj_read():
    adjectives = pd.read_csv("/home/kekeli/Desktop/PyProjects/PassPicker/english-adjectives.csv")
    adj = adjectives.iloc[random.randrange(0,1347),0]
    adj = str(adj)
    return(adj)

# Defining a function to generate a random number     
def random_num():
    number = random.randrange(0,900)
    number = str(number)
    return(number)

# Defining a function to generate a random character from 
# the given list.
def charread():
    charaters = ["~","!","@","#","$","%","^","&","*","_","-",":",";","|","/",">","<"]
    char = random.choice(charaters)
    char = str(char)
    return(char)
    