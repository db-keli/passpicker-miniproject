from password import *

welcome()
while True:   
    nounread()
    adj_read()
    random_num()
    charread()
    print ("Password is: " + nounread() + adj_read() + charread() + random_num())
    response = input("\nWant some more? Type y or n: \n")
    print("\n")
    if response == "n":
        break
