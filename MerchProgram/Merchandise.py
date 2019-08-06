# Program Description: The following program will calculate expenses and final take home revenue.

def main():
    airandbaggage()
def airandbaggage():
    members_list = ["Member 1", "Member 2", "Member 3", "Member 4"]
    totalair = 0
    totalbaggage = 0
    for member in members_list:
        airfare = float(input("How much was your airfare " + member+ "? $"))
        totalair += airfare
    for member in members_list:
        baggage = float(input('What is the weight of your baggage ' +member+ '? '))
        if baggage > 50:
            overlimit = (baggage - 50) * 4.25
            totalbaggage += overlimit
            print('Your baggage weight is over the limit of 50 lbs. There will be an additional charge.')
        elif baggage <= 50:
            print('Your baggage weight is less than 50 lbs. There will be no charge.')
    print()
    Tshirts = float(input('Please enter the number of T-Shirts sold at SXSW: '))
    Totebags = float(input('Please enter the number of Tote Bags sold at SXSW: '))
    Bobbleheads = float(input('Please enter the number of Bobblehead Dolls sold at SXSW: '))
    Tshirt_cost = Tshirts * 22
    Totebag_cost = Totebags * 18
    Bobbleheads_cost = Bobbleheads * 25
    Totalmerch = Tshirt_cost + Totebag_cost + Bobbleheads_cost
    Creditfee = Totalmerch * .025
    financials(totalair, totalbaggage, Creditfee)
    revenue(Totalmerch)
def financials(totalair, totalbaggage, Creditfee):
    Homerental = 2000
    Vanrental = 500
    Perdiem = 440
    Expenses = Homerental + Vanrental + Perdiem + totalair + totalbaggage + Creditfee
    print()
    print('Expenses:')
    print('\tItem          \tCost')
    print('\tAir Tickets:\t$', format(totalair, '.2f'))
    print('\tBaggage:\t$', format(totalbaggage, '.2f'))
    print('\tHome Rental:\t$', format(Homerental, '.2f'))
    print('\tVan Rental:\t$', format(Vanrental, '.2f'))
    print('\tPer Diem Total:\t$', format(Perdiem, '.2f'))
    print('\tCredit Fee:\t$', format(Creditfee, '.2f'))
    print()
    print('\tTotal Expenses:\t$', format(Expenses, '.2f'))
    print('*****************************************************************************')
def revenue(Totalmerch):
    Honorarium = 5500
    Revenues = Totalmerch + Honorarium
    print()
    print('Revenues:')
    print('\tItem          \tRevenue')
    print('\tMerchandise:\t$',format(Totalmerch, '.2f'))
    print()
    print('\tTotal Revenues:\t$', format(Revenues, '.2f'))
    print()
    print('************************YOU ALL DID AMAZING!!!!*******************************')
    print('We hope this program allowed you to compare your expenses and revenues!')
main()
    
    
