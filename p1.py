class GroupLimitError(Exception):
    def __init__(self, message="Досягнуто максимальну кількість студентів у групі (10)."):
        super().__init__(message)

class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age} years old, {self.gender}"

class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()}, Record Book: {self.record_book}"

class Group:
    MAX_STUDENTS = 10

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= Group.MAX_STUDENTS:
            raise GroupLimitError()
        self.group.add(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def __str__(self):
        all_students = "\n".join(str(student) for student in self.group)
        return f"Number: {self.number}\n{all_students}"

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Male', 22, 'John', 'Doe', 'AN146')
st4 = Student('Female', 23, 'Jane', 'Smith', 'AN147')
st5 = Student('Male', 27, 'Michael', 'Brown', 'AN148')
st6 = Student('Female', 21, 'Anna', 'White', 'AN149')
st7 = Student('Male', 24, 'Chris', 'Davis', 'AN150')
st8 = Student('Female', 22, 'Karen', 'Johnson', 'AN151')
st9 = Student('Male', 26, 'James', 'Wilson', 'AN152')
st10 = Student('Female', 28, 'Emily', 'Clark', 'AN153')
st11 = Student('Male', 20, 'Tom', 'Anderson', 'AN154')

gr = Group('PD1')

for student in [st1, st2, st3, st4, st5, st6, st7, st8, st9, st10]:
    gr.add_student(student)
print(gr)

try:
    gr.add_student(st11)
except GroupLimitError as e:
    print(e)
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод пошуку повинен повертати екземпляр'

gr.delete_student('Taylor')
print(gr)

gr.delete_student('Taylor')
