class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")

    def have_birthday(self):
        self.age += 1

# Creating instances (objects) of the Person class
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# Accessing object attributes and calling methods
print(person1.name)  # Output: Alice
print(person2.age)   # Output: 25

person1.introduce()  # Output: Hi, I'm Alice and I'm 30 years old.
person2.introduce()  # Output: Hi, I'm Bob and I'm 25 years old.

person1.have_birthday()
print(person1.age)  # Output: 31
