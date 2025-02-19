size = input("what size of pizza do you want? S, M or L \n")
peparoni = input("do you want extra peparoni in your pizza? Y or N")
chesse = input("do you want extra chesse in your pizza? Y or N")
bill = 0

if size == "S":
    bill +=15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("you type worng input")

if peparoni == "Y":
    if size == "S":
       bill +=2
    else:
       bill +=3 

if chesse == "Y":
   bill += 1

print(f"your final bill is {bill}")