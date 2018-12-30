#Project making baby conversation, using 3.7.2

from random import choice

#the way is call random choice
#import random
#random.choice()
#choice()

questions = ["Why is the sky blue?:", "Why is there a face on the moon?:","Where are all teh dinasours?:"]
question = choice(questions)
answer = input(question).strip().lower()

while answer != "just because":
    answer = inut("why?:").strip().lower()

print("Oh... Okay")
