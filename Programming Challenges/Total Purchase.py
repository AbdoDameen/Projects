item1 = float(input("Price for item 1: "))
item2 = float(input("Price for item 2: "))
item3 = float(input("Price for item 3: "))
item4 = float(input("Price for item 4: "))
item5 = float(input("Price for item 5: "))

all_items=(item1+item2+item3+item4+item5)



sales_tax =  0.07 * all_items
subtotal = all_items
total_amount = all_items + sales_tax

print("Subtotal is: " + format(subtotal, '.2f'))
print("Sales Tax is: " + format(sales_tax, '.2f'))
print("Total amount is: " +format(total_amount, ".2f"))
