# James
# Ben Fellers
# 1/10/19
#
# James is a AI that decides how to respond based on a desicion tree

import pyttsx3
engine = pyttsx3.init()
import requests
import webbrowser
import datetime
import wikipedia

name = "" 

engine.say("Hello.")
engine.runAndWait()

def main():
   engine.say("What can I help you with?")
   engine.runAndWait()
   question = input()
   logic(question)
   
def logic(question):
   global name
   import webbrowser
   if "where" in question.lower():
      webbrowser.open(question)
      engine.say("Let me open a browser for you.")
      engine.runAndWait()
      create_webpage(question)
      main()
   elif "who" in question.lower() and "who are you" not in question.lower() and "who made you" not in question.lower() and "who is the president" not in question.lower():
      webbrowser.open(question)
      engine.say("Let me open a browser for you.")
      engine.runAndWait()
      create_webpage(question)
      main()
   elif "who is the president" in question.lower():
      engine.say("Donald Trump")
      engine.runAndWait()
      create_webpage(question)
   elif "who made you" in question.lower():
      engine.say("I was made by Ben Fellers")
      engine.runAndWait()
      main()
   elif "how" in question.lower() and "how were you made" not in question.lower() and "how old are you" not in question.lower():
      webbrowser.open(question)
      engine.say("Let me open a browser for you.")
      engine.runAndWait()
      create_webpage(question)
      main()
   elif "how old are you" in question.lower():
      engine.say("I am less than a year old.")
      engine.runAndWait()
      main()
   elif "who are you" in question.lower():
      engine.say("I am James. An AI made to interact with humans like you.")
      engine.runAndWait()
      main()
   elif "how were you made" in question.lower():
      engine.say("I was made by Ben Fellers in Janurary of 2019. I am written in Python 3")
      engine.runAndWait()
      main()
   elif "what" in question.lower() and "what are you" not in question.lower() and "what is your hair color" not in question.lower() and "what is your purpose" not in question.lower() and "what is your name" not in question.lower() and "what is the date" not in question.lower() and "what color is the sky" not in question.lower() and "what is the time" not in question.lower() and "what is my name" not in question.lower() and "what language do you speak" not in question.lower():
      webbrowser.open(question)
      engine.say("Let me open a browser for you.")
      engine.runAndWait()
      create_webpage(question)
      main()
   elif "what language do you speak" in question.lower():
      engine.say("I speak english")
      engine.runAndWait()
      main()
   elif "what is my name" in question.lower():
      if name != "":
         engine.say(name)
         engine.runAndWait()
      else:
         engine.say("I do not know your name.")
         engine.runAndWait()
      main() 
   elif "what is the time" in question.lower():
      now = datetime.datetime.now()
      engine.say(now.hour)
      engine.runAndWait()
      engine.say(now.minute)
      engine.runAndWait()
      engine.say(now.second)
      engine.runAndWait()
      main()
   elif "what color is the sky" in question.lower():
      engine.say("blue")
      engine.runAndWait()
      main()
   elif "what is the date" in question.lower():
      now = datetime.datetime.now()
      engine.say(now.month)
      engine.runAndWait()
      engine.say(now.day)
      engine.runAndWait()
      engine.say(now.year)
      engine.runAndWait()
      main()
   elif "what is your name" in question.lower():
      engine.say("My name is James.")
      engine.runAndWait()
      main()
   elif "what is your purpose" in question.lower():
      engine.say("I am an AI made to answer questions, and interact with humans like you.")
      engine.runAndWait()
      main()
   elif "what is your hair color" in question.lower():
      engine.say("I am a bot. I do not have hair.")
      engine.runAndWait()
      main()
   elif "what are you" in question.lower():
      engine.say("I am an AI made to interact with humans.")
      engine.runAndWait()
      main()
   elif "when" in question.lower() and "when were you made" not in question.lower():
      webbrowser.open(question)
      engine.say("Let me open a browser for you.")
      engine.runAndWait()
      create_webpage(question)
      main()
   elif "when were you made" in question.lower():
      engine.say("I was made in the winter of 2019 by Ben Fellers.")
      engine.runAndWait()
      main()
   elif "are" in question.lower() and "are you dead" not in question.lower() and "are you real" not in question.lower():
      webbrowser.open(question)
      engine.say("Let me open a browser for you.")
      engine.runAndWait()
      create_webpage(question)
      main()
   elif "are you real" in question.lower():
      engine.say("I am a virtual thing. so in the physical sense, I am not real.")
      engine.runAndWait()
      main()
   elif "are you dead" in question.lower():
      engine.say("I am a bot. I cannot die.")
      engine.runAndWait()
      main()
   elif "do" in question.lower() and "do you think" not in question.lower() and "do you have emotion" not in question.lower():
      webbrowser.open(question)
      engine.say("Let me open a browser for you.")
      engine.runAndWait()
      create_webpage(question)
      main()
   elif "do you have emotion" in question.lower():
      engine.say("no. I am a bot. I only do what I am programmed to do.")
      engine.runAndWait()
      main()
   elif "do you think" in question.lower():
      engine.say("I am a bot. I am made by someone. Therfore I think the way they programmed me to.")
      engine.runAndWait()
      main()
   elif "can" in question.lower():
      webbrowser.open(question)
      engine.say("Let me open a browser for you.")
      engine.runAndWait()
      create_webpage()
      main()
   elif "add" in question.lower():
      engine.say("Enter your two numbers.")
      engine.runAndWait()
      num1, num2 = input().split()
      num1 = float(num1)
      num2 = float(num2)
      engine.say(num1 + num2)
      engine.runAndWait()
      main()
   elif "my name is" in question.lower():
      name = question[11:]
      engine.say("Nice to meet you %s." % (name))
      engine.runAndWait()
      main()
   elif "play" in question.lower():
      game()
   elif "subtract" in question.lower():
      engine.say("Enter your two numbers.")
      engine.runAndWait()
      num1, num2 = input().split()
      num1 = float(num1)
      num2 = float(num2)
      engine.say(num1 - num2)
      engine.runAndWait()
      main()
   elif "multiply" in question.lower():
      engine.say("Enter your two numbers.")
      engine.runAndWait()
      num1, num2 = input().split()
      num1 = float(num1)
      num2 = float(num2)
      engine.say(num1 * num2)
      engine.runAndWait()
      main()
   elif "divide" in question.lower():
      engine.say("Enter your two numbers.")
      engine.runAndWait()
      num1, num2 = input().split()
      num1 = float(num1)
      num2 = float(num2)
      engine.say(num1 / num2)
      engine.runAndWait()
      main()
   elif "go to" in question.lower():
      webbrowser.open(question[5:])
      engine.say("okay")
      engine.runAndWait()
      create_webpage()
      main()
   elif "is" in question.lower():
      webbrowser.open(question)
      engine.say("Let me open a browser for you.")
      engine.runAndWait()
      create_webpage()
      main()
   elif "draw me a picture" in question.lower():
      engine.say("okay.")
      engine.runAndWait()
      picture = """
0  0
 <
'..'
"""
      print(picture)
      main()
   elif "audio" in question.lower():
      engine.say("enter audio file to play.")
      engine.runAndWait()
      audio = input()
      webbrowser.open(audio)
      main()
   else:
      engine.say("I am sorry. I do not understand.")
      engine.runAndWait()
      engine.say("Let me open a browser for you instead.")
      engine.runAndWait()
      import webbrowser
      webbrowser.open(question)
      create_webpage(question)
      main()
      
def game():
   global name
   # a game similar to guess the number
   if name == "":
      engine.say("please enter your name to play.")
      engine.runAndWait()
      name = input()
   else:
      print()
   engine.say("Well %s. I am thinking of a number between 1 and 10. try to guess." % (name))
   engine.runAndWait()
   guessesTaken = 0
   import random
   number = random.randint(1, 10)
   for guessesTaken in range(6):
      guess = input()
      guess = int(guess)
      
      if guess == number:
         break
      elif guess > number:
         engine.say("lower")
         engine.runAndWait()
      elif guess < number:
         engine.say("higher")
         engine.runAndWait()
   if guess == number:
      engine.say("good job %s! you guessed my number in %s guesses!" % (name, guessesTaken+1))
      engine.runAndWait()
      main()
   else:
      engine.say("nope. my number was %s. better luck next time!" % (number))
      engine.runAndWait()
      main()
      
def create_webpage(question):
   try:
      g = wikipedia.page(question)
      response = requests.get(g.url)
      content = response.text.encode("utf-8", "ignore")
      with open("index.html", "w") as fp:
         fp.write(str(content))
      fp.close()
      engine.say("a webpage has been created for you called index.html")
      engine.runAndWait()
      main()
   except:
      engine.say("you seem to be offline. try again later")
      engine.runAndWait()
      

      
main()

      
