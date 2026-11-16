class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def grade(self):

        if self.marks >= 90:
            return "A Grade"

        elif self.marks >= 75:
            return "B Grade"

        elif self.marks >= 50:
            return "C Grade"

        else:
            return "Fail"

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Grade:", self.grade())


s1 = Student("raina", 95)
s2 = Student("jaddu", 80)

s1.display()
s2.display()