purchase_amount = float(input("Please enter the amount of purchase_amount: "))

state_tax = purchase_amount* 0.05

country_tax = purchase_amount* 0.025

total = purchase_amount+state_tax+country_tax

print("Purchase Amount = " + format(purchase_amount, ".3f")+"$")
print("State Tax = "+ format(state_tax, ".3f")+"$")
print("Country Tax = "+ format(country_tax, ".3f")+"$")
print("Total Amount ="+ format(total, ".3f" )+"$")
