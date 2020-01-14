#! /usr/bin/env python3


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        self.greet()

    def greet(self):
        print("Hi, I'm a Person, my name is %s and my age is %d" % (self.name, self.age))


class Worker(Person):
    def __init__(self, name, age, hours):
        Person.__init__(self, name, age)
        self.hours = hours

    def run(self):
        Person.greet(self)
        self.work()

    def work(self):
        print(f"Working all day...for {self.hours} hours")


class Student(Person):
    def __init__(self, name, age, subject):
        Person.__init__(self, name, age)
        self.subject = subject

    def run(self):
        Person.greet(self)
        self.study()

    def study(self):
        print(f"Study {self.subject} smarter, not harder {self.name}!")


class God(Worker, Student):
    def __init__(self, name, age, hours, subject):
        Person.__init__(self, name, age)
        Worker.__init__(self, name, age, hours)
        Student.__init__(self, name, age, subject)

    def run(self):
        Person.greet(self)
        Worker.work(self)
        Student.study(self)


if __name__ == "__main__":
    p1 = God("John", 30, 6, "Python")
    p1.run()
    print()
    p2 = Worker("Joe", 40, 8)
    p2.run()
    print()
    p3 = Student("Jane", 25, "Math")
    p3.run()
    print()
    p4 = Person("Peter", 35)
    p4.run()
    print()

    print("Classes MRO: ")
    print(Person.__mro__)
    print(Student.__mro__)
    print(Worker.__mro__)
    print(God.__mro__)
