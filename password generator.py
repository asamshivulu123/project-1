import random
char="abcdefghijklmnopqrstuvwxyABCDEFGHIJKLMNOPQRSTUVWXYZz123456789;@!':,.?/|\][{}($%)#!^*&"
while True:
    password_count=int(input("enter how many passwords do you want:"))
    password_len=int(input("enter your password length:"))
    for i in range(0,password_count):
        password=""
        for j in range(0,password_len):
            password_char=random.choice(char)
            password=password+password_char
        print("Here is your password:",password)

