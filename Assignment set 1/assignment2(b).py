# class building
class Building:
    # construstor to intiialize all variables
    def __init__(self, building_no, building_name, location, rooms = []):
        self.building_no = building_no
        self.building_name = building_name
        self.location = location
        self.rooms = rooms

    # get building no
    def get_building_no(self):
        return self.building_no

    # get building name
    def get_building_name(self):
        return self.building_name

    # get building location
    def get_location(self):
        return self.location

    # set building no
    def set_building_no(self, building_no):
        self.building_no = building_no

    # set building name
    def set_building_name(self, building_name):
        self.building_name = building_name

    # set building location
    def set_location(self, location):
        self.location = location

    # get rooms
    def get_rooms(self):
        return self.rooms

    # set rooms
    def set_rooms(self, room):
        self.rooms.append(room)

# class Room
class Room:
    # constuctor to initialize room class varialbles
    def __init__(self, room_number, room_color):
        self.room_number = room_number
        self.room_color = room_color


    # get room number
    def get_room_number(self):
        return self.room_number

    # get room color
    def get_room_color(self):
        return self.room_color

    # set room number
    def set_room_number(self, room_number):
        self.room_number = room_number

    # set room color
    def set_room_color(self, room_color):
        self.room_color = room_color

# class Department
class Department:
    # constructor to initialize department class veriables
    def __init__(self, department_name, department_head, office_location, professors = []):
        self.department_name = department_name
        self.department_head = department_head
        self.office_location = office_location
        self.professors = professors

    # get department name
    def get_department_name(self):
        return self.department_name

    # get department head
    def get_depaertment_head(self):
        return self.department_head

    # get office location
    def get_office_location(self):
        return self.office_location

    # get professors 
    def get_professors(self):
        return self.professors

    # set department name
    def set_department_name(self, department_name):
        self.department_name = department_name

    # set department head
    def set_department_head(self, department_head):
        self.department_head = department_head

    # set office location
    def set_office_location(self, office_location):
        self.office_location = office_location

    # Add professor to the department
    def set_professor(self, professor):
        self.professors.append(professor)

# class Professor
class Professor:
    # constructor to initialize professor class
    def __init__(self, professor_name, professor_id, salary):
        self.professor_name = professor_name
        self.professor_id = professor_id
        self.salary = salary

    # get professor name
    def get_professor_name(self):
        return self.professor_name

    # get professor id
    def get_professor_id(self):
        return self.professor_id

    # get professor salary
    def get_salary(self):
        return self.salary

    # set professor name
    def set_professor_name(self, professor_name):
        self.professor_name = professor_name

    # def set professsor id
    def set_professor_id(self, professor_id):
        self.professor_id = professor_id

    # set professor salary
    def set_salary(self, salary):
        self.salary = salary