import student
def main():
    students = make_list()
    print('Here is the data you entered:')
    display_list(students)
def make_list():
    student_list = []
    print('Enter data for 5 students including yourself.')
    for count in range(1, 6):
        student_name = input('Enter the student\'s first and last name: ')
        identification = input('Enter the student\'s ID number: ')
        student_gpa = input('Enter the student\'s GPA: ')
        expected = input('Enter the student\'s expected grade: ')
        full_part = input('Enter if the student is "Full Time" or "Part Time": ')
        print()
        mystudents = student.Student(student_name, identification, student_gpa, expected, full_part)
        student_list.append(mystudents)
    return student_list
main()
def print_data(mystudents):
    print(mystudents)    
    print()
