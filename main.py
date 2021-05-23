# Program Tip Calculator - Day 02 of 100

print("Welcome to the Tip Calculator...")
bill = float(input("Enter the Total Bill Amount: $"))
tip = float(input("Enter Tip percentage you want to give like ? (10, 12, or 15 or whatever you might wanna give) "))
total_bill = (bill + (bill*tip) / 100)
persons = int(input("How many people to split the bill ? "))
if persons == 0:
    final_bill = total_bill
else:
    final_bill = round(total_bill/persons, 2)
final_bill = "{:.2f}".format(final_bill)
print(f"Each person should pay: ${final_bill}")