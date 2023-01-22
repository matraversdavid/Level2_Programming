#names = ["Dave", "Simon", "Ben", "Mitchell", "Jim"]
#user_name = input("Enter a name")
#capitalised_name = user_name.title()
#if names.count(capitalised_name):
#    print("Your name is in the list")
#else:
#    print("Your name is not in the list")

#user_num = int(input("Enter a number"))
#if  user_num % 2 == 0:
#    print("This is an even number")
#else:
#    print("This is an odd number")

salary = float(input("Enter your salary"))


if salary > 50000:
    print("you pay" ,salary * 0.5 , "tax. Your income is" ,salary - salary * 0.5)
elif salary < 50000 and salary > 40000:
    print("you pay" ,salary * 0.4, "tax. Your income is" ,salary - (salary * 0.4))
else:
    print("you pay", salary * 0.3, "tax. Your income is", salary - (salary * 0.3))