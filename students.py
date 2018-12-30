#Project for creating a database of students using Python 3.7.2


#list of students
students = {
        "Alice":{"id": "ID0001" ,"age" = 26, "grade" = "A"},
        "Bob":{"id": "ID0002" ,"age" = 27, "grade" = "B"},
        "Claire":{"id": "ID0003" ,"age" = 17, "grade" = "C"},
        "Dan":{"id": "ID0004" ,"age" = 21, "grade" = "D"},
        "Emma":{"id": "ID0005" ,"age" = 22, "grade" = "E"} 
        }

#print the ID of Claire
print(students["Claire"]["id"])

#print the age of Dan
print(students["Dan"]["age"])

#print the id and grades of Emma
print(students["Emma"]["id"], students["Emma"]["grade"]
