import datetime
currentDate = datetime.datetime.now()

deadline= input ('Plz enter your date of birth (mm/dd/yyyy) ')
deadlineDate= datetime.datetime.strptime(deadline,'%m/%d/%Y')
print (deadlineDate)
daysLeft = deadlineDate - currentDate
print(daysLeft)

years = ((daysLeft.total_seconds())/(365.242*24*3600))
yearsInt=int(years)

months=(years-yearsInt)*12
monthsInt=int(months)

days=(months-monthsInt)*(365.242/12)
daysInt=int(days)

print('You are {0:d} years, {1:d}  months, {2:d}  days'.format(yearsInt,monthsInt,daysInt))