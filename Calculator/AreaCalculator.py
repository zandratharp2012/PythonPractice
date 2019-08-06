# Program Description: Area Calculator

print('Hello! This system will help you calculate the areas of a rectangle, square, and a circle.')
length = int(input('What is the length of the rectangle? '))
tries = 1
while length <= 0 and length <=10:
    print('Please enter a value greater than 1 but less than 10.', end = " ")
    length = int(input('What is the length of the rectangle? '))
    tries = tries + 1
    if tries >=3:
        print('program ends')
    else:
        width = int(input('What is the width of the rectangle? '))
        
