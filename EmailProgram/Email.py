# Program Description: This program is going to have user input email and set limitations on input. 

def main():
    email()
    name()
def email():
    email = input('Please enter your email address: ')
    position = email.find('@')
    while position != -1:
        print('The character \'@\' was found at index', position)
        break
    else:
        print('The character\'@\' was not found.')
        print('That is an invalid email. Please try again.')
        email = input('Please enter your email address: ')
    print('The email you entered is', email)
    while email [-4] != '.' and position == '@':
        print('That is an invalid email.')
        email = input('Please enter a valid email: ')
    else:
        print('Thank you for your entry')
    return email
def name():
    name = input('Please enter your USERNAME: ')
    while len(name) < 5:
        print('Your USERNAME must be longer than 5 characters.')
        name = input('Please re-enter you USERNAME.: ')
    else:
        print('Thank you for that information. We can proceed.')
    return name
main()
