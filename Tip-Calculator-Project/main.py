#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇 
print("Welcome to the tip calculator.")
total_bill = input("What was the total bill? $")
tip_percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")
no_of_people = input("How many people to split the bill? ")

tb_as_float = float(total_bill)
tp_as_float = float(tip_percentage)
np_as_int = int(no_of_people)

tip_split = tb_as_float * (tp_as_float / 100) / np_as_int
bill_split = tb_as_float / np_as_int

total_bill_and_tip = tip_split + bill_split

tbt_rounded = "{:.2f}".format(total_bill_and_tip)

print(f"Each person should pay: ${tbt_rounded}")



























