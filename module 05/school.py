class Student:
    def __init__(self, name, current_class, id):
        self.name = name
        self.current_class = current_class
        self.id = id
    
    def __repr__(self):
        return f'Student with name: {self.name}, class: {self.current_class}, id: {self.id}'


class Teacher:
    def __init__(self, name, subject, id):
        self.name = name
        self.subject = subject
        self.id = id

    def __repr__(self):
        return f'Teacher: {self.name}, Subject: {self.subject}, id: {self.id}'


class School:
    def __init__(self, name):
        self.name = name
        self.teachers = []
        self.students = []

    def add_teacher(self, name, subject):
        id = len(self.teachers) + 101
        teacher = Teacher(name, subject, id)
        self.teachers.append(teacher)

    def enroll(self, name, fee):
        if fee < 6500:
            return 'not enough fee'
        else:
            id = len(self.students) + 1
            student = Student(name, 'C', id)
            self.students.append(student)
            return f'{name} is enrolled with id: {id}, extra money {fee - 6500}'

    def __repr__(self):
        print('welcome to', self.name)
        print('------OUR TEACHERS-----')
        for teacher in self.teachers:
            print(teacher)
        print('------OUR STUDENTS-----')
        for student in self.students:
            print(student)
        return 'all done for now'


# alia = Student('Alia Bhat', 9, 1)
# ranbir = Teacher('Ranbir kapor', 'Algorithm', 101)
# print(alia)
# print(ranbir)

phitron = School('Phitron')
phitron.enroll('Alia', 5200)
phitron.enroll('Rani', 8000)
phitron.enroll('Salman Khan', 7000)
phitron.enroll('Vaijan', 90000)

phitron.add_teacher('Tom Cruise', 'Algo')
phitron.add_teacher('Decap', 'DS')
phitron.add_teacher('AJ', 'Database')

print(phitron)