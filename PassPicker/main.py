#!/usr/bin/python3
from password import passcode
from time import *

passcode.welcome()
while True:   
    print ("Password is: " + passcode.nounread() + passcode.adj_read() + passcode.charread() + passcode.random_num())
    response = input("\nWant some more? Type y or n: \n")
    print("\n")
    if response == "n":
        break
    elif response == "y" or response == "Y":
        continue
    else:
        print("Invalid response, Please make sure it's y or n.")
        response = input("Want some more?\n")
        if response == "n":
            break
