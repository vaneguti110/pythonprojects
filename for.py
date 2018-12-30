#Project to know how many vowels and consonants are in the word Hello,  using python 3.7.2

vowels = 0
consonants = 0

print("In the word 'Hello', how many vowels and consonants has:")
for letter in "Hello":
    if letter.lower() in "aeiou":
        vowels = vowels + 1
    elif letter == "":
        pass
    else:
        consonants = consonants + 1

print("There are {} vowels".format(vowels))
print("There are {} consonants".format(consonants))
