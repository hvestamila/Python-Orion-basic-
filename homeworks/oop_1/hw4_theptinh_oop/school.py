# 5. Create a new class School with get_school_id and number_of_students instance attributes

class School:
    def __init__(self, school_id, number_of_students):
        self.school_id = school_id
        self.number_of_students = number_of_students

    def get_school_id(self):
        return self.school_id

    def get_number_of_students(self):
        return self.number_of_students