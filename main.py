#The goal of this project is to apply Time Value of Money theories to create a financial calulator 
#I will be using formulas from Financial Mathematics Actuarial Science exam as reference 
#First I will use the terminal for calculations then create a front end to create a working website 

#Import classes from other files 
#Use Flask to connect to front end.
# We're going to make the user input the down payment of the home and then the total loan to predict the monthly mortgage payments


principal  = int(input("Please enter the initial investment: "))
interest = int(input("Please enter the interest rate: "))
term = int(input("Please enter the length of your loan: "))

print(principal,interest,term)
print(principal*interest)

