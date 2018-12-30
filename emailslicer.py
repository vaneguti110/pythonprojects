#Project to slice a user email using python version 3.7.2

#Get user email address
email= input("what is your email?: ").strip()

#slice out user name
user = email[:email.index("@")]

#slice domain name
#email@ggc.com --> @ +1 to start from next one
domain = email[email.index("@")+1:]

#format message
output = "Your username is {} and your domain is {}".format(user, domain)

#display output message
print(output)
