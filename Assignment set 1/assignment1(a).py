import roman

#class library for managing books and students
class Library:
    books = []
    students = []
    
    #Add book to the library
    @staticmethod
    def add_book(book):
        Library.books.append(book)

    # remove book from the libraty
    @staticmethod
    def remove_book(book):
        Library.books.remove(book)

    # show all the book
    @staticmethod
    def show_books():
        for i, x in enumerate(Library.books):
            print(f"{i + 1}). Book: {x.name}, Author: {x.author}")

    # add student to the library
    @staticmethod
    def add_student(student):
        Library.students.append(student)

    # remove student from library
    @staticmethod
    def remove_student(student):
        Library.students.remove(student)

    # SHOW ALL THE STUDENTS
    @staticmethod
    def show_students():
        for i, x in enumerate(Library.students):
            print(f"{i + 1}). {x.name}")

    # Show details of all the students
    @staticmethod
    def __str__():
        for i, s in enumerate(Library.students):
            print(f"{chr(97 + i)}. Student {s.name} has borrowed {len(s.borrowed_books)} and the details are as follows:")
            for j, b in enumerate(s.borrowed_books):
                print(f'\t{roman.toRoman(j+1)}. Book-{j+1} with title "{b.name}" and Author is "{b.author}"')

# class book
class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author
        Library.add_book(self)


# class Student
class Student:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []
        Library.add_student(self)

    # student Borrow book from library
    def borrow_book(self, book):
        self.borrowed_books.append(book)

    # student returns the book to libarary
    def return_book(self, book):
        self.borrowed_books.remove(book)

if __name__ == '__main__':

    # creating book Instance
    b1 = Book("Python Programming", "Json Rees")
    b2 = Book("Networking", "Tanenbaum")
    b3 = Book("Database", "Korth")
    # Library.show_books()

    # adding student and borrowing the books
    s1 = Student("Alia")
    s1.borrow_book(b1)
    s1.borrow_book(b2)
    s2 = Student("Ahmad")
    s2.borrow_book(b3)
    # Library.show_students()

    Library.__str__()