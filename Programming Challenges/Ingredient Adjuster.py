number_of_cookies = float(input("How many are you trying to make: "))

sugar = 0.0312
flour = 0.0573
butter = 0.0208

sugar_amout = sugar * number_of_cookies
flour_amout = flour * number_of_cookies
butter_amount = butter * number_of_cookies

print("You would need "+ format(sugar_amout, '.2f') + " cup of sugar")
print("You would need "+ format(flour_amout, '.2f') + " cup of flour")
print("You would need "+ format(butter_amount, '.2f') + " cup of butter")
