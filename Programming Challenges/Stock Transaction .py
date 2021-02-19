num_stocks = 2000
buy = 40.00
sell = 42.75
commis = 0.03


paid = num_stocks * buy
sold = num_stocks * sell
buy_commis = commis * paid
sell_comms = commis * sold



print("Joe Paid "+ '$'+format(paid, ',.2f')+ ' for the stocks'+ " and paid "+'$'+ format(buy_commis, ',.2f')+" commisson")
print("Joe sold the stock for "+'$'+format(sold, ',.2f')+ " and paid "+ format(sell_comms, ',.2f')+" commisson")

total = sold - paid - buy_commis - sell_comms

if total > 0:
    print("Joe made a profit of "+'$'+format(total, ',.2f'))
else:
    print('Joe made a Loss of '+'$'+format(total, ",.2f"))
