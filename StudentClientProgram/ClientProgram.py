# Program DescriptionL This program will have a class that stores information. You are able to look up information, change information and print information.

import client_list
import pickle
LOOK_UP = 1
ADD = 2
CHANGE_LAST = 3
CHANGE_ACCBAL = 4
COR_ADDRESS = 5
SEARCH_LAST = 6
PRINT_DATA = 7
HELP_OP = 8
QUIT = 9
FILENAME = 'client_file.dat'
def main():
    myclients = load_clients()
    choice = 0
    while choice != QUIT:
        choice = get_menu_choice()
        if choice == LOOK_UP:
            look_up(myclients) 
        elif choice == ADD:
            add(myclients)
        elif choice == CHANGE_LAST:
            change(myclients)
        elif choice == CHANGE_ACCBAL:
            change(myclients)
        elif choice == COR_ADDRESS:
            change(myclients)
        elif choice == SEARCH_LAST:
            search(myclients)
        elif choice == PRINT_DATA:
            print_data(myclients)
        elif choice == HELP:
            help_op(myclients)
    save_clients(myclients)
def load_clients():
    try:
        input_file = open(FILENAME, 'rb')
        client_dct = pickle.load(input_file)
        input_file.close()
    except IOError:
        client_dct = {}
    return client_dct
def get_menu_choice():
    print()
    print("MENU")
    print("***************************************************")
    print('1. Look up and print the client name and address')
    print('2. Add a new client')
    print('3. Change the Last Name of a client')
    print('4. Change the account balance of a client')
    print('5. Correct a street address')
    print('6. Search for a client by last name')
    print('7. Print the data of all the clients')
    print('8. Get help')
    print('9. Quit the program')
    print()
    choice = int(input('Please enter your choice, 1-9: '))
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input("Please enter a valid choice, 1-4: "))
    return choice
def look_up(myclients):
    name = input('Enter the client\'s name: ')
    print(myclients.get(name, add))
def add(myclients):
    lname = input('Enter the new client\'s last name: ')
    fname = input('Enter the new client\'s first name: ')
    add = input('Enter the new client\'s address: ')
    city = input('Enter the new client\'s city of residence : ')
    zipc = input('Enter the new client\'s zipcode : ')
    phone = input('Enter the new client\'s phone number : ')
    email = input('Enter the new client\'s email: ')
    accnum = input('Enter the new client\'s account number: ')
    numacc = input('Enter the new client\'s number of accounts: ')
    bal = input('Enter the new client\'s primary account balance: ')
    print()
    entry = client.Client(lname, fname, add, city, zipc, phone, email, accnum, numacc, bal)
    if lname not in myclients:
        myclient[lname] = entry
        print('The entry has been added.')
        print()
    else:
        print('That name already exists.')
        print()
def print_data(client_list):
    for clients in client_list:
        print('Client Last Name:', myclients.get_lname())
        print('Client First Name:', myclients.get_fname())
        print('Client Street Address:', myclients.get_add())
        print('Client City:', myclients.get_city())
        print('Client Zip Code:', myclients.get_zipc())
        print('Client Phone Number:', myclients.get_phone())
        print('Client Email:', myclients.get_email())
        print('Client Account Number:', myclients.get_accnum())
        print('Client Number Of Accounts:', myclients.get_numacc())
        print('Client Primary Account Balance:', myclients.get_bal())
def save_clients(myclients):
    output_file = open(FILENAME, 'wb')
    pickle.dump(myclients, output_file)
    output_file.close()
main()




        
