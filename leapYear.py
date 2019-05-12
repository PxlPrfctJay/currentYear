# A Program that has three functions to return a day of year
#Function One:
# A function that checks if a given year is a leap year

#Function Two:
# A function that returns number of days in month
# (28,29,30,31) depending on the given month(1-12) and year
# which uses isYearLeap(year) to determine a leap year

#Function Three:
# A function that returns a day of the year in month/day/year format
# It will return 'None' if the given day is more than 31 or less than 1
# It will return a Type if month is more than 12 or less than 1



def isYearLeap(year):
    #check if year is equally divisible by 4
    if(year%4==0):
        #if year divisible by 4, check if divisble by 100
        if(year%100==0):
            #if year divisible by 100 check if year alos divisible by 400 
            #if true year is leap and return True
            if(year%400==0):
                return True
            #if not divisible by 400 return false, not a leap year
            else:
                return False
        #if not divisible by 100 but by 4, return true for leap year
        else:
            return True
    #if not divisible by 4, return false for no leap year 
    else:
        return False

def daysInMonth(year, month):
    #create two lists to account for 30 day months and 31 day months
    thirtyDays = [4,6,9,11]
    thirtyOneDays = [1,3,5,7,8,10,12]
    
    #run given month thru if statements to determine number of days in month
    
    if(month in thirtyOneDays):
        #return 31 if the given month is in thirtyOneDays list
        return 31
    elif(month in thirtyDays):
        return 30
        #return 30 if the given month is in thirtyDays list
    elif(month==2):
        #Since month is Feb, check if year is Leap, 29 if yes, 28 if not.
        if(isYearLeap(year)):
            return 29
        else:
            return 28
 

def dayOfYear(year, month, day):
    #check if given day is valid, if not return None
    if(day>(daysInMonth(year, month)) or day<1):
        return None
 
    else:
        #return the day of year in month/day/year format
        return "{}/{}/{}".format(month,day,year)

#call Function Three
print(dayOfYear(2020, 12, 29))