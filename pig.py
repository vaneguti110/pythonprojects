#Project called pig latin translator uses a word, takes the first consonant and put it to the end of the vowels an change the word completely, using python 3.7.2

#get sentence from user
original = input("Please enter a sentence:").strip().lower()

#split sentence into words
words = original.split()
print(words)

#loop through words and convert to pig latin
new_words = []

for word in words:
    #if starts with a vowel, just add "yay"
    if word[0] in "aeiou":
        new_word = word + "yay"
        new_words.append(new_word)
    #otherwise, move the first consonant cluser to the end, and "ay"
    else:
        vowel_pos = 0
        for letter in word:
            if letter not in "aeiou":
                vowel_pos = vowel_pos + 1
            else:
                break
        #the consonant is safe
        cons = word[:vowel_pos]
        print ("The consonant(s) is/are:",cons)
        #the rest of the word left
        the_rest = word[vowel_pos:]
        new_word = the_rest + cons + "ay"
        new_words.append(new_word)
            

#stick words back together
output = "".join(new_words)

#output the final string
print("The final word using the pig latin translator is", output)
