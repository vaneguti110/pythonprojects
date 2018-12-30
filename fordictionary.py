#Project to create a dictionary of students and show the students who has a letter "a" in it, using python 3.7.2

students = {
    "male":["Tom", "Charlie", "Harry", "Frank"],
    "female":"Sarah", "Huda", "Samantha", "Emily", "Elizabeth"]
}

for key in students.keys():
    for name in students[key]:
        if "a" in name:
            print(name)
