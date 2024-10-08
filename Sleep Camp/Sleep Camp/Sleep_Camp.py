class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

    def authenticate(self, entered_password):
        return self.password == entered_password

    def is_student(self):
        return self.role == "student"

    def is_instructor(self):
        return self.role == "instructor"


class Student:
    def __init__(self, student_id, name, age):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)
        course.enroll_student(self)

    def __str__(self):
        return f"Student ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Courses: {[course.name for course in self.courses]}"


class Course:
    def __init__(self, course_code, name, instructor, tuition_fees, timetable):
        self.course_code = course_code
        self.name = name
        self.instructor = instructor
        self.students = []
        self.tuition_fees = tuition_fees
        self.timetable = timetable

    def enroll_student(self, student):
        self.students.append(student)

    def __str__(self):
        return f"Course Code: {self.course_code}, Name: {self.name}, Instructor: {self.instructor}, Tuition Fees: {self.tuition_fees} Rands, Timetable: {self.timetable}"


class SleepCampUniversity:
    def __init__(self):
        self.users = []
        self.students = []
        self.courses = []

    def register_user(self):
        username = input("Enter your desired username: ")
        while any(user.username == username for user in self.users):
            print("Username already exists. Please choose another one.")
            username = input("Enter your desired username: ")

        password = input("Enter your password: ")
        role = input("Are you a student or instructor? ").lower()

        user = User(username, password, role)
        self.users.append(user)
        print(f"User {username} registered successfully!")

    def register_course(self):
        course_code = input("Enter the course code: ")
        name = input("Enter the course name: ")
        instructor = input("Enter the instructor's name: ")
        tuition_fees = float(input("Enter the tuition fees for the course (in Rands): "))
        timetable = input("Enter the class timetable: ")

        course = Course(course_code, name, instructor, tuition_fees, timetable)
        self.courses.append(course)
        print(f"Course '{course.name}' registered successfully!")

    def login(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        user = next((user for user in self.users if user.username == username and user.authenticate(password)), None)
        return user

    def view_timetable(self):
        print("Available Courses:")
        for course in self.courses:
            print(course)

    def handle_student_actions(self, student):
        print(f"Welcome, {student.username}!")
        print(f"1. Enroll Courses:")
        print("2. View Timetable")
        self.view_timetable()
        print("3. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            self.Enroll_course()
        elif choice == "2":
            self.view_timetable()
        elif choice == "3":
            print("Exiting. Goodbye!")
            exit()
        else:
            print("Invalid choice. Please try again.")

    def handle_instructor_actions(self, instructor):
        print(f"Welcome, {instructor.username}!")
        print("1. Register Course")
        print("2. View Timetable")
        print("3. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            self.register_course()
        elif choice == "2":
            self.view_timetable()
        elif choice == "3":
            print("Exiting. Goodbye!")
            exit()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    sleep_camp_university = SleepCampUniversity()

    while True:
        print("1. Register\n2. Login\n3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            sleep_camp_university.register_user()
        elif choice == "2":
            logged_in_user = sleep_camp_university.login()

            if logged_in_user:
                if logged_in_user.is_student():
                    new_varnew_var = sleep_camp_university.handle_student_actions(logged_in_user)
                    
                elif logged_in_user.is_instructor():
                    sleep_camp_university.handle_instructor_actions(logged_in_user)
            else:
                print("Invalid username or password. Please try again.")
        elif choice == "3":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
