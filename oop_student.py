class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class student(person):
    def __init__(self,name,age,number,score):
        person.__init__(self,name,age)
        self.number = number
        self.score = score

    def display(self):
        print("name is " + self.name)
        print("age is " + str(self.age))
        print("number is " + self.number)
        print("score is " + str(self.score))

stud1 = student("Tom", 84, "S100", 84)
stud1.display()

stud2 = student("Anne", 64, "S200", 64)
stud2.display()