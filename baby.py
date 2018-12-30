#Project making baby conversation, using python idle version 3.7.2
#Ask random questions about baby questions, it will stop asking when you said just just because

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
