#Imports data from other file
from accounts import accounts

name = input("Enter username: ")
password = input("Enter password: ")

if name in accounts:#checking name exists in dictionary
    if password == accounts[name]:#checking password user enters matches value in dictionary
        print("Welcome", name)
    else:
        print("Wrong password")
else:
    print("Username doesn't exist")