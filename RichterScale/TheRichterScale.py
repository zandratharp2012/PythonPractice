# Program Description: This program will read informatiom and place richter scale information in a table format. 

def main():
    email()
    name()
    displayTable()
    inputRichter()
    print('We will send this information to the email address provided.')
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
def displayTable():
    infile = open('richters.txt', 'r')
    line = infile.readlines()
    infile.close()
    index = 0
    myList = []
    for num in line:
        myList.append(float(num))
        for y in myList:
            richter = y
        myList.sort()
        print(format('Richter                                Joules                                          TNT'))
        Joules = float(10**((1.5 * richter)+4.8))
        newfile = open('earthquakesZandraTharp.txt', 'w')
        newfile.write(str(Joules) + '\n')
        TNT = float((Joules * 2.390057361377) * (10** -7) / 1000)
        print(richter,'                            ', Joules, '                        ', TNT)
    print('==========================================================================================================')
    print('Your file has been saved to: earthquakesZandraTharp.txt')
    newfile.close()
def inputRichter():
    tries = 0
    print('==========================================================================================================')
    Richter = float(input('Please enter the desired scale measurement on the Richter scale greater than 1 but not greater than 10: '))
    while (Richter > 1 or Richter <= 10) and tries < 3:
            if Richter >= 1 and Richter <= 4:
                print('That was nothing! You could still go out for a run!')
                break
            elif Richter >=5 and Richter <= 8:
                print('Ok, that definitely was not just in my head!')
                break
            elif Richter >= 8 and Richter <= 10:
                print('Time to run with the wind and get on our of here!')
                break
            else:
                print('Wrong, Try Again!')
                Richter = float(input('Please enter the desired scale measurement on the Richter scale greater than 1 but not greater than 10: '))
                tries = tries + 1
                if tries >= 3:
                    print('You are only allowed 3 incorrect entries. Too many incorrect entries. Please restart the program.')
    Energy(Richter)
def Energy(Richter):
    inputEnergy = float(10**((1.5 * Richter)+4.8))
    while Richter != 0.0:
        inputEnergy = float(10**((1.5 * Richter)+4.8))
        print('With your Selection of', Richter, 'The Energy produced in Joules is: ')
        print(format(inputEnergy, '.2e'))
        print('More specifically, the Energy produced in Joules is equal to: ', \
        format(inputEnergy, '<20'))
        break
    Tnt(inputEnergy, Richter)
def Tnt(inputEnergy, Richter):
        Tnt = float((inputEnergy * 2.390057361377) * (10** -7) / 1000)
        print('With your selection on the Richter Scale, this much TNT in tons was produced: ', \
            format(Tnt, '.2e'))
        print('More specifically, the TNT in tons produced is equal to: ', \
            format(Tnt, '<20'))
        print('That is a great amount of Energy and TNT!!', end = ' ')
        while Richter <= 1 or Richter > 10:
             print()
             break      
main()
