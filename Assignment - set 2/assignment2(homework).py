# class Department
class Department:
    # constructor to initialize Depeartment Class instance object
    def __init__(self, name, code):
        self.department_name = name
        self.department_code = code
        self.courses = []

    # get department name
    def get_department_name(self):
        return self.department_name

    # get department code
    def get_department_code(self):
        return self.department_code

    # get courses
    def get_courses(self):
        return self.courses

    # set department name
    def set_department_name(self, department_name):
        self.department_name = department_name

    # set department code
    def set_department_code(self, department_code):
        self.department_code = department_code

    # set course
    def set_course(self, course):
        self.courses.append(course)

# classs Course
class Course:
    # initialize course obhect
    def __init__(self, description, code, credit):
        self.description = description
        self.code = code
        self.credit = credit
        self.registerd_students = []

    # get description
    def get_description(self):
        return self.description

    # get code
    def get_code(self):
        return self.code

    # get credit
    def get_credit(self):
        return self.credit

    # get registered students
    def get_registered_student(self):
        return self.registerd_students

    # set descriptions 
    def set_description(self, description):
        self.description = description

    # set code
    def set_code(self, code):
        self.code = code

    # set credit
    def set_credit(self, credit):
        self.credit = credit

    # set registered srudents
    def set_registered_student(self, student):
        self.registerd_students.append(student)   

# class student
class Student:
    # Student constuctor to initialize object
    def __init__(self, name, student_number):
        self.name = name
        self.student_number = student_number

    # get student name
    def get_name(self):
        return self.name

    # get student number
    def get_student_number(self):
        return self.student_number

    # set student name
    def set_name(self, name):
        self.name = name

    # set student number
    def set_student_number(self, number):
        self.student_number = number

if __name__ == "__main__":
    d = Department("Mechanical", '107')

    c1 = Course("Fluid Mechanics", 479654, 6)
    c2 = Course("Heat Exchange and Transformaion", 469876, 8)
    c3 = Course("Internal Combustion Engine", 469264, 8)
    
    d.set_course(c1)
    d.set_course(c2)
    d.set_course(c3)

    s1 = Student("Narendra", 17107769258)

    c1.set_registered_student(s1)
    c2.set_registered_student(s1)
    c3.set_registered_student(s1)

    s2 = Student("Amit", 17107769153)

    c1.set_registered_student(s2)
    c2.set_registered_student(s2)
    c3.set_registered_student(s2)


    print("Name of Department:", d.get_department_name(), "Department Code: ", d.get_department_code())
    for i, course in enumerate(d.get_courses()):
        print(f"\t{i+1}). Course Name: {course.get_description()}, Course Credit: {course.get_credit()}, Course Code: {course.get_code()}")
        print("\tRegistered Students")
        for j, student in enumerate(course.get_registered_student()):
            print(f"\t\t{j+1}). Student Name: {student.get_name()}, Student Number: {student.get_student_number()}") 