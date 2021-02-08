import random
class StudentCourse:
    def __init__(self, student_name, course_name, scores=[], weights=[], assignment_names=[]):
        self.student_name = student_name
        self.course_name = course_name
        self.scores = []
        self.weights = []
        self.assignment_names = []
    
    def add_assignment(self, score, weight=1.0, name=None):
        self.scores.append(score)
        self.weights.append(weight)
        self.assignment_names.append(name)
    
    def get_grade(self):
        if(self.scores):
            return sum(score * weight for score, weight in zip(self.scores, self.weights)) / sum(self.weights)
        else:
            return 1.0
    
    def get_scores(self):
        return self.scores
    
    def print_grades(self):
        print('  Course: ' + self.course_name)
        print('    scores, weights, assignment names')
        for i in range(len(self.scores)):
            print('   ', '%.2f' % (self.scores[i] * 100) + '%', self.weights[i], self.assignment_names[i])
        print('    Grade: %.2f' % (self.get_grade() * 100) + '%')

class Gradebook:
    def __init__(self, student_names):
        self.data = {name: dict() for name in student_names}
        self.student_names = student_names
        self.all_courses = set()
    
    def add_course(self, student_name, course_name):
        self.data[student_name][course_name] = StudentCourse(student_name, course_name)
        self.all_courses.add(course_name)
    
    def add_score(self, student_name, course_name, score, weight=1.0, name=None):
        self.data[student_name][course_name].add_assignment(score, weight, name)
    
    def get_student_names(self):
        return self.student_names
    
    def get_all_courses(self):
        return self.all_courses
    
    def get_data(self):
        return self.data
    
    def print_gradebook(self):
        for key, value in self.data.items():
            print('Student: ', key)
            for course in value.values():
                course.print_grades()

if __name__ == '__main__':
    grades = Gradebook(['John', 'Liam', 'Olivia', 'Oliver', 'Emma', 'Ava', 'William', 'Sophia'])
    for name in grades.get_student_names():
        grades.add_course(name, 'Math')
        grades.add_score(name, 'Math', 1.0 - random.random() * 0.1)
        grades.add_score(name, 'Math', 2.0 - random.random() * 0.1)
    
    grades.print_gradebook()