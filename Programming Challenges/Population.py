intinal_number = float(input("Please enter the Starting number of the Population: "))
avg_daily_incr = float(input("A verage Daily Increase: "))


number_days = int(input('Number of days to multiply: '))


print(intinal_number, avg_daily_incr, number_days)
app_pop = (intinal_number * avg_daily_incr)  / 100

daily_increase = intinal_number
for i in range(number_days):
    print("Day "+str(i +1)+ ' '+ "        "+str(daily_increase))
    app_pop = (daily_increase * avg_daily_incr)  / 100
    daily_increase = app_pop + daily_increase
