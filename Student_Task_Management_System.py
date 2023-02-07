from datetime import datetime
from bst_demo import BSTDemo, Node

print("******** PROGRAMMED BY ********")
print("****** Charlotte Quezada ******")
print("********** BSCOE 2-2 **********")
print("*** Sir Danilo Madrigalejos ***\n")


def get_task_input_details():
    start_time = input("Enter the time in hh:mm format (example 18:30 or 6:30): ")
    while True:
        try:
            datetime.strptime(start_time, '%H:%M')
        except ValueError:
            print("Incorrect time format, it should be hh:mm")
            start_time = input("Enter the time in hh:mm format (example 18:30 or 6:30): ")
        else:
            break
    duration_of_task = input("Enter the duration of the task in minutes (example 60): ")
    while True:
        try:
            int(duration_of_task)
        except ValueError:
            print("Please enter a valid number for number of minutes.")
            duration_of_task = input("Enter the duration of the task in minutes (example 60):  ")
        else:
            break
    task_name = input("Enter the name of the task (case sensitive): ")
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

    # Function Delete Student: The user can permanently delete a student's record
    def delete_student(self, first_n, last_n, student_no, course, address, phone):
        for student in self.students_list:
            if student.first_n == first_n or student.last_n == last_n or student.student_no == student_no \
                    or student.course == course or student.address == address or student.phone == phone:
                self.students_list.remove(student)

    # Function View Students: The user can view the full list of the students
    def list_students(self):
        print("\n                              * * * View Students * * *                        \n")
        counting = len(self.students_list)
        print("               Number of Students Recorded In The Student Task Management System:", counting, "\n")
        if not self.students_list:
            print("No students found.\n")
        for student in self.students_list:
            student.print_student()

    # Function Search Student: The user can search a student by searching its student information
        # – either name, student number, course, address, and contact number
    def search_students(self, search_item):
        for student in self.students_list:
            if search_item == student.first_n or search_item == student.last_n or search_item == student.student_no \
                    or search_item == student.course or search_item == student.address or search_item == student.phone:
                student.print_student()
                break
            if not search_item == self.students_list:
                print("Student not found. \n")


# This class serves as a data storage that will contain all student information
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

    # Function Print Student: It displays / prints the student information
    def print_student(self):
        print("-" * 60)
        print("* * Student Information * *")
        print("""Name: %s\nStudent Number: %s\nCourse: %s\nAddress: %s\nPhone Number: %s""" %
              (self.first_n.upper() + " " + self.last_n.upper(), self.student_no, self.course.upper(),
               self.address.upper(), self.phone))
        print("-" * 60 + "\n")


class StudentManageInput:
    def __init__(self):
        self.StudentFunction = StudentFunction()

    def user_student_info(self):
        first_n = input("Enter the first name of the student: ")
        last_n = input("Enter the last name of the student: ")
        student_no = input("Enter the student number of the student: ")
        while True:
            try:
                int(student_no)
            except ValueError:
                print("Please enter a valid number for student number.")
                student_no = input("Enter the student number of the student: ")
            else:
                break
        course = input("Enter the course of the student: ")
        address = input("Enter the address of the student: ")
        phone = input("Enter the phone number of the student: ")
        while True:
            try:
                int(phone)
            except ValueError:
                print("Please enter a valid number for phone number.")
                phone = input("Enter the phone number of the student: ")
            else:
                break
        return first_n, last_n, student_no, course, address, phone

    def add_student_to_students(self):
        print("\n                        * * * ADD STUDENT * * *                        \n")
        first_n, last_n, student_no, course, address, phone = self.user_student_info()
        self.StudentFunction.add_student(first_n, last_n, student_no, course, address, phone)
        while True:
            if first_n == "" and last_n == "" and student_no == "" and course == "" and address == "" and phone == "":
                print("Error! Please fill all the fields.")
            else:
                print("Student added, we have saved the student's information successfully!\n")
            add_again = input("Would you like to add another student? Type y/n: ")
            if add_again.lower() == "y" or add_again.lower() == "yes":
                first_n, last_n, student_no, course, address, phone = self.user_student_info()
                self.StudentFunction.add_student(first_n, last_n, student_no, course, address, phone)
                continue
            elif add_again.lower() == "n" or add_again.lower() == "no":
                print("Returning to the main menu of the Student Task Management System...\n")
                self.run_menu()
                break

    def edit_student_from_students(self):
        print("\n                        * * * EDIT STUDENT * * *                        \n")
        done = False
        final_done = False
        search_item = " "
        first_n = " "
        last_n = " "
        student_no = " "
        course = " "
        address = " "
        phone = " "
        new_first_n = " "
        new_last_n = " "
        new_student_no = " "
        new_course = " "
        new_address = " "
        new_phone = " "
        option = " "
        while not done:
            print("Which Student in the Student Task Management System do you want to edit?")
            print("""   Choose an option below to locate the student.   
               (a) First Name
               (b) Last Name
               (c) Student Number
               (d) Course
               (e) Address
               (f) Phone Number""")
            edit1_option = input("Enter the option you choose (a-f): ")
            if edit1_option.lower() == "a":
                search_item = input("Enter the first name of this student: ")
                first_n = search_item
            elif edit1_option.lower() == "b":
                search_item = input("Enter the last name of this student: ")
                last_n = search_item
            elif edit1_option.lower() == "c":
                search_item = input("Enter the student number of this student: ")
                student_no = search_item
            elif edit1_option.lower() == "d":
                search_item = str(input("Enter the course of this student: "))
                course = search_item
            elif edit1_option.lower() == "e":
                search_item = input("Enter the address of this student: ")
                address = search_item
            elif edit1_option.lower() == "f":
                search_item = str(input("Enter the phone number of this student: "))
                phone = search_item
            else:
                print("Please enter a valid input!")
                continue
            print("Would you like to enter more information? Type y/n: ")
            done = input() == "n"
        print("Searching for the student, please wait...")
        self.StudentFunction.search_students(search_item)
        confirm = input("Would you like to continue editing? Type y/n: ")
        if confirm.lower() == "y":
            while not final_done:
                print("""   What information from this student do you want to edit?   
                   (a) First Name
                   (b) Last Name
                   (c) Student Number
                   (d) Course
                   (e) Address
                   (f) Phone Number""")
                edit2_option = input("Enter the option you choose (a-f): ")
                if edit2_option.lower() == "a":
                    new_first_n = input("Enter the new first name of this student: ")
                elif edit2_option.lower() == "b":
                    new_last_n = input("Enter the new last name of this student: ")
                elif edit2_option.lower() == "c":
                    new_student_no = input("Enter the student number of this student: ")
                elif edit2_option.lower() == "d":
                    new_course = str(input("Please enter the course of this student: "))
                elif edit2_option.lower() == "e":
                    new_address = input("Enter the new address of this student: ")
                elif edit2_option.lower() == "f":
                    new_phone = str(input("Enter the new phone number of this student: "))
                else:
                    print("Please enter a valid input!")
                    continue
                print("Do you want to save the changes you edited for this student? Type y/n: ")
                final_done = input() == "y"
                option = edit2_option
            self.StudentFunction.edit_student(first_n, new_first_n, last_n, new_last_n, student_no, new_student_no,
                                              course, new_course, address, new_address, phone, new_phone,
                                              option)
            print("Changes in the student have been saved successfully!")
            print("Returning to the main menu of the Student Task Management System...\n")
            self.run_menu()
        elif confirm.lower() == "n":
            print("Student is not edited in the Student Task Management System.")
            print("Returning to the main menu of the Student Task Management System...\n")
            self.run_menu()

    def delete_student_from_students(self):
        print("\n                       * * * DELETE STUDENT * * *                       \n")
        done = False
        search_item = " "
        first_n = " "
        last_n = " "
        student_no = " "
        course = " "
        address = " "
        phone = " "
        while not done:
            print("Which Student in the Student Task Management System do you want to delete?")
            print("""   Choose an option below to locate the student.   
               (a) First Name
               (b) Last Name
               (c) Student Number
               (d) Course
               (e) Address
               (f) Phone Number""")
            del_option = input("Enter the option you choose (a-f): ")
            if del_option.lower() == "a":
                search_item = input("Enter the first name of this student: ")
                first_n = search_item
            elif del_option.lower() == "b":
                search_item = input("Enter the last name of this student: ")
                last_n = search_item
            elif del_option.lower() == "c":
                search_item = input("Enter the student number of this student: ")
                student_no = search_item
            elif del_option.lower() == "d":
                search_item = str(input("Enter the course of this student: "))
                course = search_item
            elif del_option.lower() == "e":
                search_item = input("Enter the address of this student: ")
                address = search_item
            elif del_option.lower() == "f":
                search_item = str(input("Enter the phone number of this student: "))
                phone = search_item
            else:
                print("Please enter a valid input!")
                continue
            print("Would you like to enter more information? Type y/n: ")
            done = input() == "n"
        print("Searching for the student, please wait...")
        self.StudentFunction.search_students(search_item)
        confirm = input("\nAre you sure you want to continue to delete? Type y/n: ")
        if confirm.lower() == "y":
            self.StudentFunction.delete_student(first_n, last_n, student_no, course, address, phone)
            print("Student deleted successfully in the Student Task Management System!")
            print("Returning to the main menu of the Student Task Management System...\n")
            self.run_menu()
        elif confirm.lower() == "n":
            print("Student is not deleted in the Student Task Management System.")
            print("Returning to the main menu of the Student Task Management System...\n")
            self.run_menu()

    def create_search(self):
        print("\n                        * * * SEARCH STUDENT * * *                        \n")
        done = False
        search_item = " "
        while not done:
            print("Which Student in the Student Task Management System do you want to search?")
            print("""   Choose an option below to locate the student.   
               (a) First Name
               (b) Last Name
               (c) Student Number
               (d) Course
               (e) Address
               (f) Phone Number""")
            respond = input("Enter the option you choose (a-f): ")
            if respond.lower() == "a":
                search_item = input("Enter the first name of this student: ")
            elif respond.lower() == "b":
                search_item = input("Enter the last name of this student: ")
            elif respond.lower() == "c":
                search_item = input("Enter the student number of this student: ")
            elif respond.lower() == "d":
                search_item = str(input("Enter the course of this student: "))
            elif respond.lower() == "e":
                search_item = input("Enter the address of this student: ")
            elif respond.lower() == "f":
                search_item = str(input("Enter the phone number of this student: "))
            else:
                print("Please enter a valid input!")
                continue
            print("Would you like to enter more information? Type y/n: ")
            done = input() == "n"
        print("Searching for the student, please wait...")
        self.StudentFunction.search_students(search_item)
        print("Going back to the main menu of the Address Book...\n")
        self.run_menu()

    def manage_task_to_student(self):
        print("\n                       * * * MANAGE TASK * * *                       \n")
        done = False
        search_item = " "
        first_n = " "
        last_n = " "
        student_no = " "
        course = " "
        address = " "
        phone = " "
        while not done:
            print("Which Student in the Student Task Management System do you want to manage task?")
            print("""   Choose an option below to locate the student.   
               (a) First Name
               (b) Last Name
               (c) Student Number
               (d) Course
               (e) Address
               (f) Phone Number""")
            task_option = input("Enter the option you choose (a-f): ")
            if task_option.lower() == "a":
                search_item = input("Enter the first name of this student: ")
                first_n = search_item
            elif task_option.lower() == "b":
                search_item = input("Enter the last name of this student: ")
                last_n = search_item
            elif task_option.lower() == "c":
                search_item = input("Enter the student number of this student: ")
            elif task_option.lower() == "d":
                search_item = str(input("Enter the course of this student: "))
            elif task_option.lower() == "e":
                search_item = input("Enter the address of this student: ")
            elif task_option.lower() == "f":
                search_item = str(input("Enter the phone number of this student: "))
            else:
                print("Please enter a valid input!")
                continue
            print("Would you like to enter more information? Type y/n: ")
            done = input() == "n"
        print("Searching for the student, please wait...")
        self.StudentFunction.search_students(search_item)
        confirm = input("Would you like to continue managing task? Type y/n: ")
        if confirm.lower() == "y":
            format_item = str(search_item).upper()
            print("Tasks Registered to "f"{format_item}\n")
            with open("data.txt") as f:
                for line in f:
                    my_tree.insert(line)
            while True:
                print("\nPlease choose an option from the list below:")
                print("|| 1 ||     View Today's Scheduled Tasks")
                print("|| 2 ||     Add a Task to Today's Schedule")
                print("|| 3 ||     Delete a Task from the Schedule")
                print("|| 4 ||     Return to Main Menu")
                selection = input("\nEnter your choice: ")
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
                    if num == my_tree.length() - 1:
                        with open("data.txt", "a+") as to_write:
                            to_write.write(line + "\n")
                    input("Press any key to continue... ")
                elif int(selection) == 3:
                    print("\n* * * * * * * * * * * * * * DELETE  TASK * * * * * * * * * * * * * *\n")
                    print("You have chosen to delete a task from the schedule")
                    start_time, duration_of_task, task_name = get_task_input_details()
                    key_to_find = datetime.strptime(start_time, '%H:%M').time()
                    result = my_tree.find_val(key_to_find)
                    if result:
                        if result.name_of_task == task_name and result.duration == duration_of_task:
                            print("Deleting task: ")
                            print(result)
                            my_tree.delete_val(key_to_find)
                            print("Task successfully deleted.")
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
                    print("\n* * * * * * * * * * * *  RETURN TO MAIN MENU * * * * * * * * * * * *\n")
                    print("Returning to the main menu of the Student Task Management System...\n")
                    self.run_menu()
                else:
                    print("Please enter a number between 1 and 4")
        elif confirm.lower() == "n":
            print("No changes in managing task in the Student Task Management System.")
            print("Returning to the main menu of the Student Task Management System...\n")
            self.run_menu()

    def option_from_main_menu(self, option):
        if option == "1":
            self.add_student_to_students()
            return True
        elif option == "2":
            self.edit_student_from_students()
            return True
        elif option == "3":
            self.delete_student_from_students()
            return True
        elif option == "4":
            self.StudentFunction.list_students()
            return True
        elif option == "5":
            self.create_search()
            return True
        elif option == "6":
            self.manage_task_to_student()
            return True
        elif option == "7":
            confirm = input("\nAre you sure you want to exit the Student Task Management System? Type y/n: ")
            if confirm.lower() == "y" or confirm == "yes":
                print("\n          Thank you for using this Student Task Management System.          "
                      "\n                                 Goodbye!                                   ")
                exit()
            elif confirm.lower() == "n" or confirm == "no":
                print("Returning to the main menu of the Student Task Management System...\n")
                self.run_menu()
            else:
                print("Please enter a valid answer.")
                confirm = input("\nAre you sure you want to exit the Student Task Management System Type y/n: ")
                if confirm.lower() == "y" or confirm == "yes":
                    print("\n          Thank you for using this Student Task Management System.          "
                          "\n                                 Goodbye!                                   ")
                    exit()
                elif confirm.lower() == "n" or confirm == "no":
                    print("Returning to the main menu of the Student Task Management System...\n")
                    self.run_menu()
            return False
        else:
            print("\nInvalid option, please enter an option correctly!\n")
            self.run_menu()
            return True

    def run_menu(self):
        running = True
        while running:
            print("***~~~***~~~*~*~~*~*~*~*~*~~*~*~***~*~*~~*~*~*~*~*~~*~*~~~******~~~***")
            print("                   Student Task Management System                     ")
            print("***~~~***~~~*~*~~*~*~*~*~*~~*~*~***~*~*~~*~*~*~*~*~~*~*~~~******~~~***")
            welcome = "                          Welcome Student!                        \n"
            main_menu = """What would you like to do?
               ||  1  ||    Add Student         
               ||  2  ||    Edit Student        
               ||  3  ||    Delete Student       
               ||  4  ||    View Students 
               ||  5  ||    Search Student       
               ||  6  ||    Manage Task  
               ||  7  ||    Exit                 """
            print(welcome)
            print("MAIN MENU")
            print(main_menu)
            option = input("Enter the option you choose: ")
            running = self.option_from_main_menu(option)


def main():
    """ Main program """
    runner = StudentManageInput()
    runner.run_menu()
    return 0


if __name__ == "__main__":
    main()
