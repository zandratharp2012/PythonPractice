# Program Description: This program will hold data about a student, print information and place in tabular format.

import student
import student_list
import pickle
LOOK_UP = 1
ADD = 2
PRINT_DATA = 3
QUIT = 4
FILENAME = 'student_file.dat'
def main():
    mystudents = load_students()
    choice = 0
    while choice != QUIT:
        choice = get_menu_choice()
        if choice == LOOK_UP:
            look_up(mystudents) 
        elif choice == ADD:
            add(mystudents)
        elif choice == PRINT_DATA:
            print_data(student_list)
    save_students(student_list)
def load_students():
    try:
        input_file = open(FILENAME, 'rb')
        student_dct = pickle.load(input_file)
        input_file.close()
    except IOError:
        student_dct = {}
    return student_dct
def get_menu_choice():
    print()
    print("MENU")
    print("***************************************************")
    print("1. Look up and print a student's GPA")
    print("2. Add a new student to the class")
    print("3. Print the data of all the students")
    print("4. Quit the program")
    print()
    choice = int(input("Please enter your choice, 1-4: "))
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input("Please enter a valid choice, 1-4: "))
    return choice
def look_up(mystudents):
    gpa = input("Enter a GPA: ")
    if gpa not in mystudents:
        print('GPA exists.')
def add(mystudents):
    name = input('Enter the new student\'s name: ')
    ident = input('Please enter the student\'s ID number: ')
    gpa = input('Please enter the student\'s GPA: ')
    grade = input('Please enter the student\'s expected grade: ')
    hours = input('Please enter if this student is "Full Time" or "Part Time": ')
    print()
    entry = student.Student(name, ident, gpa, grade, hours)
    if name not in mystudents:
        mystudents[name] = entry
        print('The entry has been added.')
        print()
    else:
        print('That name already exists.')
        print()
def print_data(student_list):
    print(student_list)
    print()
def save_students(mystudents):
    output_file = open(FILENAME, 'wb')
    pickle.dump(mystudents, output_file)
    output_file.close()
main()




        
