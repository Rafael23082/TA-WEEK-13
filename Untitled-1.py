from Store import course
from Store import student

def main():
    x = course()
    y = student()
    add_more_courses = True
    count = 1
    print("--------------------------------------")
    print("University Course Registration System")
    print("--------------------------------------")
    print("ENTER THE DETAILS OF THE COURSES PRESENT IN THE UNIVERSITY")
    while add_more_courses == True:
        course_code=str(input("Enter the course code of the course "))
        x.couse_code[f"Course {count}: "] = course_code
        title = str(input("Enter the title of the course: "))
        x.title[f"Title of course {count}: "] = title
        maximum_capacity = int(input("Enter the maximum capacity of students for the course: "))
        num_of_students = int(input("Enter the number of students in the course: "))    
        x.maximum_capacity[f"Maximum Capacity of course {count}: "] = maximum_capacity
        x.num_of_students[f"Current number of students for course {count}: "] = num_of_students
        x.check_availability[course_code] = [maximum_capacity , num_of_students]
        if maximum_capacity <= num_of_students:
            x.full_courses.append(course_code)
        else:
            pass
        check = str(input("Do you want to enter more courses? enter Yes if you want to and No otherwise ")) 
        if check.lower() == "yes":
            add_more_courses = True
            count += 1
        else:
            add_more_courses = False

    name = str(input("Enter the name of the student "))
    y.name = name
    id = int(input("Enter the student ID "))
    y.id = id

    y.display_student_info()
    x.enroll_student()
    x.display_courses()
    x.check_courses_capacity()
    
main()