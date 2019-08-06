# Program Description: Coin Exchange Sim 

print('Hello! Welcome to the Zandra Coin Changer where all your dreams come true!')
half_dollars = float(input('How many half dollars do you have? '))
quarters = float(input('How many quarters do you have? '))
dimes = float(input('How many dimes do you have? '))
nickels = float(input('How many nickels do you have? '))
pennies = float(input ('How many pennies do you have? '))
#Convert data to dollars.
total = float((half_dollars * .50) + (quarters * .25) + (dimes * .10) + (nickels * .05) + (pennies * .01))
#Display total number of dollars
print('Your total amount is $', total)
#Calculate total with fees and tax
print('We cannot forget the taxes and fees as we need to make money too!')
after_tax = float(total - (total * .01))
fees = float(after_tax - (after_tax * .0477))
print('Your total after taxes is $', \
      format(after_tax, '.2f'))
print('Your total after fees is $', \
      format(fees, '.2f'))
print('Thank you and we hope to see you and your coins soon!')
