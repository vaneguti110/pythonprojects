#Project called cinema simulator, check the list of films, check if user is allow to see a film and enough seats available to watch the film, using Python version 3.7.2
#Example in the idle:
#It needs to write one of this film when asking you for a film to run: "Finding Dory","Bourne","Tarzan","Ghost Busters"

#data of films dictionary
films = {
    "Finding Dory":[3,5],
    "Bourne":[18,5],
    "Tarzan":[15,5],
    "Ghost Busters":[12,5]
    }

while True:
    choice = input("What film would you like to watch?:").strip().title()

    if choice in films:
        age = int(input("How old are you?:").strip())

        #check user age
        if age >= films[choice][0]:
            
            #check enough seats
            num_seats = films[choice][1]
            
            if num_seats > 0:
                print("Enjoy the film!")
                films[choice][1] = films[choice][1] - 1
            else:
                print("Sorry, we are sold out!")            
        else:
            print("You are too young to see that film!")
    else:
        print("We don't have that film...")
