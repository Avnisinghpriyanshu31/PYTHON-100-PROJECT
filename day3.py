# number = int(input("check the number is even or odd:"))
# if number % 2 ==0:
#     print("the number is even")
# else:
#      print("the number is odd")



print("welcome to bada wala jhula\n")
height = int(input("tera height kya hai be?\n"))
bill = 0
if height >120:
    print("tum bada wala jhula jhul skte ho!\n")
    age = int(input("tera age kya hai \n"))
    if age >=18:
        bill = 12
        print(f"tera ticket ${bill}ka hua")
    elif age<= 12:
        bill =5
        print(f"tera ticket ${bill} ka hua bache")
    else:
        bill =7
        print(f"tera ticket ${bill} ka hua")
    want_photo = input("do you want photo, yes or no\n")
    if want_photo == "yes":
       total_bill = bill + 3 
       print(f"your ticket price is {total_bill},including with photo price $3")
    else:
        print(f"your ticket is {bill}")
else:
    print("abe bada hoke aana jaa idhar se!")