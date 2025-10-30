#this program collects the bill of a group of people, asks for the % tip they want to pay,
#the number of persons paying and prints each person's bill

print("Welcome to your tip calculator")

bill = float(input("Please enter your bill:  $"))
percentage_tip = int(input("What percentage tip would you like to give? 10,12 or 15?  "))
persons = int(input("How many people are splitting the bill?  "))

total_bill = bill * (1 + (percentage_tip / 100))
individual_bill = round((total_bill / persons), 2)

#using the format function to round the individual bill to 2 decimal places, including zero at the end
individual_bill = "{:.2f}". format(total_bill / persons)

print(f"Each person is to pay ${individual_bill}")