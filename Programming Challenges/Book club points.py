books = int(input("How Many books have you purchased this month? "))

if books <= 1:
    print('You earned %i points this month' % 0)
elif books> 1 and books < 4:
    print('You earned %i points this month' % 5)
elif books> 3 and books < 6:
    print('You earned %i points this month' % 15)
elif books> 5 and books < 8:
    print('You earned %i points this month' % 30)
else:
    print('You earned %i points this month' % 60)
