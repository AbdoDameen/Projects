budget = int(input("Please enter the amount you have bugeted for this month: "))

print(budget)

expensess = ['Rent','Food','Car','Gym','Phone','Travel','Savings']

balance=0
for i in expensess:
    if balance == 0:
        added_balance = int(input('How much did you budget for '+str(i)))
        new_balance = int(budget - added_balance)
        print(new_balance)
    else:
        added_balance = int(input('How much did you budget for '+str(i)))
        new_balance = int(balance - added_balance)

    balance = new_balance
    #budget = balance
    print("Current budget is "+str(balance))

if 0 > balance:
    print("You are "+format(abs(balance))+ " underbudgeted")
else:
    print('Good Job you would have extra $'+format(balance) +' to spend')
