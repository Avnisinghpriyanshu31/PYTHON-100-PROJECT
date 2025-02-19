print("welcome to tip calcutator!")
total_bill = float(input("whats was the total bill?\n$"))
tip = int(input("how much tip would you like to give? 10,15,20\n"))
contry = int(input("how much peaple to split the bill?\n"))
tip_calculated = total_bill*tip/100
bill_with_tip = tip_calculated + total_bill
final_bill = bill_with_tip/contry
final_amount = round(final_bill,2)
print(f"each person should pay : ${final_amount}")
