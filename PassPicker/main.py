from password import passcode

passcode.welcome()
while True:   
    print ("Password is: " + passcode.nounread() + passcode.adj_read() + passcode.charread() + passcode.random_num())
    response = input("\nWant some more? Type y or n: \n")
    print("\n")
    if response == "n":
        break
