import random
import pyttsx3 as engine
import datetime
time=datetime.datetime.now().strftime("%I:%M %p")
char="abcdefghijklmnopqrstuvwxyABCDEFGHIJKLMNOPQRSTUVWXYZz123456789;@!':,.?/|\][{}($%)#!^*&"

while True:

    engine.speak("hello this is password generator")
    engine.speak("please enter how many passwords do you want")

    password_count=int(input("enter how many passwords do you want:"))
    engine.speak("thank you for your response")

    engine.speak("please enter password length")

    password_len=int(input("enter your password length:"))
    engine.speak("thank you for entering password length")

    for i in range(0,password_count):

        password=""
        for j in range(0,password_len):
            password_char=random.choice(char)
            password=password+password_char
        print("Here is your password:",password)
    engine.speak("here is your passwords")

    engine.speak("thank you for visiting enjoy your day")
