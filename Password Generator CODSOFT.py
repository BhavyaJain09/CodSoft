import random

def Password_Generator(length):
    if length < 6:
        print(" Password length should be atleast 6 characters.")
        return None

    upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_letters = "abcdefghijklmnopqrstuvwxyz"
    digits = "0123456789"
    symbols = "!@#$%^&*()_+-={}:;><.?/~"

    #Combining every letter, digit and symbol that can be used to make a password 
    combine = upper_letters + lower_letters + digits + symbols

    #Generating a random password
    Password = ""
    for i in range(length):
        Password = Password + random.choice(combine)
    return Password

def main():
    print("Hi there, I'm your password Generator.")
    length = int(input("Enter the desired length of the password you want = "))

    Password = Password_Generator(length)
    if Password:
        print(f" Generated Password!: {Password}\n")
    else:
        print("Failed to generate a password.\n")
    main()

main()
