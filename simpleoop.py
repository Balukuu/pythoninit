class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def get_student_id(self):
        return self.student_id

    def set_student_id(self, student_id):
        self.student_id = student_id

# Create a Person
person1 = Person("Alice", 25)
print("Person 1 - Name:", person1.get_name(), "Age:", person1.get_age())

# Create a Student
student1 = Student("Bob", 20, "S12345")
print("Student 1 - Name:", student1.get_name(), "Age:", student1.get_age(), "Student ID:", student1.get_student_id())

# Modify attributes
person1.set_age(30)
student1.set_name("Charlie")
student1.set_student_id("S67890")

print("Person 1 - Name:", person1.get_name(), "Age:", person1.get_age())
print("Student 1 - Name:", student1.get_name(), "Age:", student1.get_age(), "Student ID:", student1.get_student_id())
