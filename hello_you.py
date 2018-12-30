#Project ask information about the user, name, age, city, what do you love doing and stores it in variable and print the message to the screen using python version 3.7.2

#Ask user for name
name = input("What is your name?: ")
print(name)

#Ask user for age
age = input("What is your age?: ")
print(age)

#Ask user for city
city = input("What city do you live in?: ")
print(city)

#Ask user what they enjoy
love = input("What do you love doing?: ")

#Create output text
string  = "Your name is {} and you are {} years old. you live in {} and you love {}"
output = string.format(name, age, city, love)

#Print output to screen
print(output)
