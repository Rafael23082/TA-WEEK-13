#course information is stored in separate files
class course:
    def __init__(self):
        self.couse_code = {}
        self.title = {}
        self.maximum_capacity = {}
        self.num_of_students = {}
        self.full_courses = []
        self.courses_enrolled =[]
        self.check_availability ={}

    def display_courses(self):
        print("LIST OF COURSES IN THE UNIVERSITY")
        for (k,v),(k2,v2),(k3,v3),(k4,v4) in zip(self.couse_code.items(), self.title.items(), self.maximum_capacity.items(), self.num_of_students.items()):
            print ("-----------------------------------------------------")
            print (k,v)
            print(k2,v2)
            print(k3,v3)
            print(k4,v4)

    def enroll_student(self):
        checkk = True
        while checkk == True:
            courses_enrolled = str(input("Enter the course codes that the student enrolled. "))
            if courses_enrolled in self.couse_code.values():
                if courses_enrolled in self.full_courses:
                    print("Course is full, you cannot enroll")
                else:
                    self.courses_enrolled.append(courses_enrolled)
                enroll = str(input("Do you want to enroll in more courses? "))
                if enroll.lower() == "yes":
                    checkk = True
                else:
                    checkk = False
            else:
                print("Course code is invalid")

    def check_courses_capacity(self):
        course_code = str(input("Enter the course code you want to check "))
        if course_code in self.couse_code.values():
            for k,v in self.check_availability.items():
                if k == course_code:
                    result = v[0] - v[1]
                    print(f"There are {result} slots left")
        else:
            print("Course code is invalid")
        

class student:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.courses_enrolled = []

    def display_student_info(self):
        print(f"Student ID: {self.id}")
        print(f"Student Name: {self.name}")

