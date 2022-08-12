# do exercise here
# upload to github for portfolio
# thank me later when your git graph is as green as the python money u gonna earn


'''# task 1 

n = 0

while n < 3: 

   Number_1 = int(input("Enter 1st number="))

   Number_2 = int(input("Enter 2nd number="))

   if Number_1 > Number_2:
       print( Number_1, "is the biggest")

   elif Number_1 < Number_2: 
       print(Number_2, "is the biggest")

   else:
       print("both are equals")

   n += 1 '''

# task 2
Months = ('January', 'February', 'March', 'April', 'May', 'June', 'July ', 'August', 'September', 'October', 'November', 'December')

Month = input("Input the name of Month:")

if Month == "February":
   print("No. of days: 28/29 days")
elif Month in ("April", "June", "September", "November"):
   print("No. of days : 30 days")
elif Month in ("January", "March", "May", "July", "August", "October", "December"):
   print("No. of days: 31 days")
else:
    print("Wrong month name")
