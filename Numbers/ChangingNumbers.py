#Program Description: This is a function to read a numbers file and modify numbers. 

#Open numbers.txt in append mode
#Read the numbers into a list
#Strip the list of the end of line markers or the "\n"
#Append the numbers 11 through 20 to this list (done in a loop)
#Write the list back to the numbers file - you will insert a tab "\t" after each number
#You will use a loop to read from and write to the file
#Write an exception that will be raised if the program is unable to open the files
def main():
    try:
        infile = open('numbers.txt', 'r')
        line = infile.readline()
        while line != '':
            print(line)
            line = line.rstrip("\n")
            line = infile.readline()
        infile.close()
        index = 0
        while index < len(line):
            line[index] = line[index]
            index += 1
        num_numbers = 10
        numberFile = open('numbers.txt', 'a')
        print('Enter the numbers you would like to add.')
        for count in range(1, num_numbers + 1):
            number = int(input('Number' + str(count) + ': '))
            numberFile.write(str(number) + '\t')
        numberFile.close()
        print('The numbers given have been saved to number.txt.')
    except Exception as err:
        print(err)
main()



