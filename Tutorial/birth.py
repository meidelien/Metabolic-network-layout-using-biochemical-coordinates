currentPop = 312032486
oneYear = 365
hours = 24
minutes = 60
seconds = 60

# seconds in a single day
secondsInDay = hours * minutes * seconds

# seconds in a year
secondsInYear = secondsInDay * oneYear

fiveYears = secondsInYear * 5

#Seconds in 5 years
print(fiveYears)

# fiveYears in seconds, divided by 7 seconds
births = fiveYears // 7

print("if there was a birth every 7 seconds, there would be {} births in a year".format(births))