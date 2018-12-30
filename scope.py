#Project about global variables, local variables and scope, using python 3.7.2

##In the idle example:
#It will display: f1=260 --> it will show be 250 + 10 since in the function is calling global variable a 
#f2=50
#a=250

a = 250

#another way with array
#a = [1,2,3]

#def f1():
    #a[0] = 5 
    #print(a) --> it will display the list with the change value [5,2,3]

def f1():
    #to call the global value => global a
    global a
    b = a + 10
    print(b)

def f2():
    a = 50 #local a
    print(a)

f1()
f2()
print(a)


##Important fact:
#
#1)Two types of scope - Global and local
#2)Python functions create local scopes
