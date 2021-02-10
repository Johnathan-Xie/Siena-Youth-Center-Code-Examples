class Person:
    def __init__(self, fname, lname, age, height=None, weight=None):
        self.firstname = fname
        self.lastname = lname
        self.height = height
        self.weight = weight
        self.age = age
        if self.height and self.weight:
            self.bmi = self.weight / (self.height ** 2)
    
    def greeting(self):
        return 'Hello ' + self.firstname + ' ' + self.lastname

class Student(Person):
    def __init__(self, fname, lname, age, school_name, height=None, weight=None):
        super().__init__(fname, lname, age, height, weight)
        self.school_name = school_name
    
    def welcome(self):
        return super().greeting() + '. Welcome to ' + self.school_name + '.'

#write another class which inherits from person and utilizes the super keyword

if __name__ == '__main__':
    me = Student('Johnathan', 'Xie', 16, 'Sacred Heart Schools Atherton')
    print(me.welcome())