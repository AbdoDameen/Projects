purchase_amount = float(input("Please enter the amount of purchase_amount: "))

number_of_installments = float(input("Please spacify how many Installments would you like to pay: "))

five = purchase_amount * 0.05

total = purchase_amount + five

installment = total/number_of_installments

print("Total Amount = "+ format(total, ".3f")+"$")
print("You would have to pay "+ format(installment, ".3f")+" $ each Installments")
