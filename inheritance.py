class Students:

    def __init__(self, student_id, student_year):
        self.student_id = student_id
        self.student_year = student_year

    def print_student_parent(self):
        print("Student name is " + self.name + " " + self.student_id + " " + self.student_year)

    def print_student(self):
        print("Student name is " + "John" + " " + self.student_id + " " + self.student_year)


class Names(Students):

    def __init__(self, name):
        self.name = name

    def print_student_child(self):
        super().__init__("23434234234", "First year")
        super().print_student_parent()


names_child = Names("John")
names_child.print_student_child()

names = Students("23434234234", "First year")
names.print_student()





