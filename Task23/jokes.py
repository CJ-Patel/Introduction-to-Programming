#CJ Patel
#Task23 - jokes.py
#------------------------------------------------------------#
#import random library
import random

#list of jokes
jokes = ['So the earth goes around the sun, and every four years it does it wrong?\nThat is...not very comforting.', 'Does my stomach think all potatoes are mashed?', '"I have never been so hungry in my entire life" - me every two hours', 'Wants: cuddles\nReceives: struggles', 'Can you lick Computer Science?\nNothing else has made the code work, so you might as well try it']

#display random joke
print(jokes[random.randint(0,len(jokes)-1)])