date = str(input('Please enter a date :dd/mm/yy '))

day = int(date.split()[0][0:2])
month = int(date.split()[0][3:5])
year = int(date.split()[0][6:9])

print(date)

if day * month == year:
    print("This date is magic!")
else:
    print('Sorry! it\'s not magic')
