class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


def main():
    student_list = []

    num_students = int(input("Enter the number of students: "))

    for i in range(num_students):
        name = input(f"Enter the name of student {i+1}: ")
        age = int(input(f"Enter the age of student {i+1}: "))
        student = Student(name, age)
        student_list.append(student)

    print("\nStudent Information:")
    for student in student_list:
        student.display_info()

if __name__ == "__main__":
    main()
