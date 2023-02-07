from datetime import datetime
from bst_demo import BSTDemo, Node


def get_task_input_details():
    start_time = input("Enter the time in hh:mm format, example 18:30 or 6:30 -> ")
    while True:
        try:
            datetime.strptime(start_time, '%H:%M')
        except ValueError:
            print("Incorrect time format, it should be hh:mm")
            start_time = input("Enter the time in hh:mm format, ex 18:30 or 6:30 -> ")
        else:
            break
    duration_of_task = input("Enter the duration of the task in minutes, ex 60 -> ")
    while True:
        try:
            int(duration_of_task)
        except ValueError:
            print("Please enter a valid number for number of minutes.")
            duration_of_task = input("Enter the duration of the task in minutes, ex 60 -> ")
        else:
            break
    task_name = input("Enter the name of the task (case sensitive)-> ")
    return start_time, duration_of_task, task_name


my_tree = BSTDemo()


class StudentFunction:
    students_list = []

    # Function Add Student: The user can add student information - name, student number, course
    # address, and contact number
    def add_student(self, first_n, last_n, student_no, course, address, phone):
        self.students_list.append(Student(first_n, last_n, student_no, course, address, phone))

    # Function Edit Student Information - The user can edit any information of the student
    def edit_student(self, first_n, new_first_n, last_n, new_last_n, student_no, new_student_no, course, new_course,
                     address, new_address, phone, new_phone, option):
        for student in self.students_list:
            if student.first_n == first_n or student.last_n == last_n or student.student_no == student_no \
                    or student.course == course or student.address == address or student.phone == phone:
                if option == "a":
                    edited_first_n = first_n.replace(first_n, new_first_n)
                    student.first_n = edited_first_n
                elif option == "b":
                    edited_last_n = last_n.replace(last_n, new_last_n)
                    student.last_n = edited_last_n
                elif option == "c":
                    edited_student_no = student_no.replace(student, new_student_no)
                    student.student_no = edited_student_no
                elif option == "d":
                    edited_course = course.replace(course, new_course)
                    student.course = edited_course
                elif option == "e":
                    edited_address = address.replace(address, new_address)
                    student.address = edited_address
                elif option == "f":
                    edited_phone = phone.replace(phone, new_phone)
                    student.phone = edited_phone
        if not self.students_list:
            print("Student not found.")

    


class Student:
    first_n = None
    last_n = None
    student_no = None
    course = None
    Address = None
    Phone = None

    def __init__(self, first_n, last_n, student_no, course, address, phone):
        self.first_n = first_n
        self.last_n = last_n
        self.student_no = student_no
        self.course = course
        self.address = address
        self.phone = phone


with open("data.txt") as f:
    for line in f:
        my_tree.insert(line)

while True:
    print("\nPlease choose an option from the list below:")
    print("|| 1 ||     View today's scheduled tasks")
    print("|| 2 ||     Add a task to today's schedule")
    print("|| 3 ||     Remove a task from the schedule")
    print("|| 4 ||     Exit")
    selection = input("\nEnter your choice -> ")
    try:
        entry = int(selection)
    except ValueError:
        print("Please enter a number between 1 and 4")
        continue
    if int(selection) == 1:
        print("\n* * * * * * * * * * * *  VIEW TASK SCHEDULE  * * * * * * * * * * * *\n")
        my_tree.in_order()
    elif int(selection) == 2:
        print("\n* * * * * * * * * * * * * * * ADD TASK * * * * * * * * * * * * * * *\n")
        print("You have chosen to add a task to the schedule")
        start_time, duration_of_task, task_name = get_task_input_details()
        line = start_time + "," + duration_of_task + "," + task_name
        num = my_tree.length()
        my_tree.insert(line)
        if num == my_tree.length()-1:
            with open("data.txt", "a+") as to_write:
                to_write.write(line+"\n")
        input("Press any key to continue... ")
    elif int(selection) == 3:
        print("\n* * * * * * * * * * * * * * REMOVE  TASK * * * * * * * * * * * * * *\n")
        print("You have chosen to remove a task from the schedule")
        start_time, duration_of_task, task_name = get_task_input_details()
        key_to_find = datetime.strptime(start_time, '%H:%M').time()
        result = my_tree.find_val(key_to_find)
        if result:
            if result.name_of_task == task_name and result.duration == duration_of_task:
                print("Removing task:")
                print(result)
                my_tree.delete_val(key_to_find)
                print("Task successfully removed")
                with open("data.txt", "r") as f:
                    lines = f.readlines()
                with open("data.txt", "w") as f:
                    for line in lines:
                        if line.strip("\n") != start_time + "," + duration_of_task + "," + task_name:
                            f.write(line)
                input("Press any key to continue... ")
            else:
                print("The name and/or duration of task did not match, delete failed")
                input("Press any key to continue... ")
        else:
            print("Task not found")
            input("Press any key to continue... ")
    elif int(selection) == 4:
        print("\n* * * * * * * * * * * * * * *   EXIT   * * * * * * * * * * * * * * *\n")
        print("Exiting program...")
        break
    else:
        print("Please enter a number between 1 and 4")
