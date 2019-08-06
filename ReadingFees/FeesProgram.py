# Program Description:  This program will read fees from a file and use a function to display file. 

def main():
    infile = open('fees.txt', 'r')
    lines = infile.readlines()
    print(lines)
    infile.close()
    print('********************************************************************************')
    index = 0
    while index < len(lines):
        lines[index] = lines[index].rstrip('\n')
        index += 1
    print(lines)
    print('********************************************************************************')
    print('Airline 1st Bag 2nd Bag Change Fee Other Fee Feels Like')
    index = 0
    list1 = []
    while index < len(lines):
        temp = index + 6
        list1.append(lines[index:temp])
        index = index + 6   
    rows = 1
    cols = 6
    for r in range(rows):
        for c in range(cols):
            print(list1[c])
main()
