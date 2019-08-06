# Program Description: This program will calculate projected profits based on sales and costs

days_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
totalEggs = 0
for day in days_list:
    eggs = int(input("How many eggs did you collect on " + day + "? "))
    while eggs > 55 or eggs < 550:
        if eggs > 55 and eggs < 550:
            totalEggs += eggs
            print(totalEggs, " eggs is the total for the week.")
            break
        else:
            print('Please enter a number greater than 55 and less than 550.')
            eggs = int(input("How many eggs did you collect on " + day + "? "))

cartons = totalEggs // 12
leftover_eggs = totalEggs % 12
print('The total cartons made is: ', cartons)
medium = int(input('How many medium cartons did you sell? '))
large = int(input('How many large cartons did you sell? '))
jumbo = int(input('How many jumbo cartons did you sell? '))
uber = int(input('How many uber cartons did you sell? '))
total_cartons = medium + large + jumbo + uber
while total_cartons != cartons:
    print('Please review the information entered')
    medium = int(input('How many medium cartons did you sell? '))
    large = int(input('How many large cartons did you sell? '))
    jumbo = int(input('How many jumbo cartons did you sell? '))
    uber = int(input('How many uber cartons did you sell? '))
    total_cartons = medium + large + jumbo + uber
    print('The total cartons entered is: ',total_cartons)

mountain = "m"
river = "r"
route = input('What route will you take today? Enter "m" for mountain or "r" for river? ')
medium_cost = medium * 4
large_cost = large * 5
jumbo_cost = jumbo * 6
uber_cost = uber * 7
total_cartons_cost = medium_cost + large_cost + jumbo_cost + uber_cost
print('******************************************************************************')
print('For the week this is what your financials look like:')
print('Expenses:')
if route == "m":
    mGasoline = float((15.13 / 6.5) * 3.99)
    mountainGas = mGasoline * 2
    print('Gasoline used for mountain route is: $', \
          format(mountainGas, '.2f'))
    totalGas = mountainGas
elif route == "r":
    rGasoline = float((12.22 / 6.5) * 3.99)
    riverGas = rGasoline * 2
    print('Gasoline used for river route is: $', \
          format(riverGas, '.2f'))
    totalGas = riverGas
    
helper_salary = 15 * 8.5
market_fee = total_cartons_cost * .01
chicken_coop = 55 * .10
chicken_upkeep = 55 * .12
chicken_totalmaint = chicken_coop + chicken_upkeep
total_expenses = helper_salary + totalGas + market_fee + chicken_coop + chicken_totalmaint
print('Expenses:')
print('     Helper Salary: $', \
          format(helper_salary, '.2f'))
print('     Market Fee: $',  \
          format(market_fee, '.2f'))
print('     Total Cost for Chicken Maintenance: $', \
      format(chicken_totalmaint, '.2f'))
print('     Total Expenses come out to: $', \
      format(total_expenses, '.2f'))
print('Total Revenue:')
print('     Egg Sales: $', format(total_cartons_cost, '.2f'))
print()
weekly_profit = total_cartons_cost - total_expenses
annual_profit = weekly_profit * 52
print('Weekly Profit:           $', format(weekly_profit, '.2f'))
print('Annual Projected Profit: $', format(annual_profit, '.2f'))  
