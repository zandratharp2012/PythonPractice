import client
def main():
    clients = make_list()
    print('Here is the data you entered:')
    display_list(clients)
def make_list():
    client_list = []
    print('Enter data for 4 students and then yourself.')
    for count in range(1, 5):
        last = input('Please enter client\'s last name: ')
        first = input('Please enter client\'s first name: ')
        address = input('Please enter client\'s address: ')
        city = input('Please enter client\'s city of residence: ')
        zipcode = input('Please enter client\'s zipcode: ')
        phone = input('Please enter client\'s phone number: ')
        email = input('Please enter client\'s email: ')
        acc_num = input('Please enter client\'s account number: ')
        num_acc = input('Please enter the number of accounts for this client: ')
        balance = input('Please enter the balance in the primary account: $')
        print()
        myclients = client.Client(last, first, address, city, zipcode, phone, email, acc_num, num_acc, balance)
        client_list.append(myclients)
    last = ('Client\'s last name: Tharp')
    first = ('Client\'s first name: Zandra')
    address = ('Client\'s address: 1234 Austin Rd')
    city = ('Client\'s city of residence: Austin')
    zipcode = ('Client\'s zip code: 78729')
    phone = ('Client\'s phone number: 123-456-789')
    email = ('Client\'s email: zandra.tharp@g.austincc.edu')
    acc_num = ('Client\'s account number: 123456')
    num_acc = ('Client\'s number of accounts: 2')
    balance = ('Balance of primary account: $1.00')
    myclients = client.Client(last, first, address, city, zipcode, phone, email, acc_num, num_acc, balance)
    client_list.append(myclients)
    print()
    return client_list
main()
def print_data(mystudents):
    print(mystudents)    
    print()
