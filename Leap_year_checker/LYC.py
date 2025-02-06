def leap(year):
    leap = False #initialzie leap as False by default
    if (year%4==0 and year%100!=0) or year%400==0: #if any of the two conditions are met it is a leap year.
        leap = True # Set leap to true if conditions are met 

        return leap # return value of leap
    
year = int(input()) # input from user 