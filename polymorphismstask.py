class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("Dog barks")


a = Dog()
a.sound()

class Employee:
    def work(self):
        print("Employee is working")


class Developer(Employee):
    def work(self):
        print("Developer writes code")


e = Developer()
e.work()

class Vehicle:
    def move(self):
        print("Vehicle is moving")


class Car(Vehicle):
    def move(self):
        print("Car is moving")


class ElectricCar(Car):
    def move(self):
        print("Electric car is moving silently")


e = ElectricCar()
e.move()

class Person:
    def introduce(self):
        print("I am a person")


class Teacher(Person):
    def introduce(self):
        print("I am a teacher")


class MathTeacher(Teacher):
    def introduce(self):
        print("I am a mathematics teacher")


m = MathTeacher()
m.introduce()

class Shape:
    def draw(self):
        print("Drawing a shape")


class Circle(Shape):
    def draw(self):
        print("Drawing a circle")


class Rectangle(Shape):
    def draw(self):
        print("Drawing a rectangle")


c = Circle()
r = Rectangle()

c.draw()
r.draw()

class BankAccount:
    def account_type(self):
        print("Bank account")


class SavingsAccount(BankAccount):
    def account_type(self):
        print("Savings account")


class CurrentAccount(BankAccount):
    def account_type(self):
        print("Current account")


s = SavingsAccount()
c = CurrentAccount()

s.account_type()
c.account_type()

class Camera:
    def feature(self):
        print("Camera feature")


class MusicPlayer:
    def feature(self):
        print("Music player feature")


class Smartphone(Camera, MusicPlayer):
    pass


s = Smartphone()
s.feature()

class Writer:
    def work(self):
        print("Writing")


class Speaker:
    def speak(self):
        print("Speaking")


class Author(Writer, Speaker):
    pass


a = Author()
a.work()
a.speak()

class Person:
    def show(self):
        print("Person")


class Student(Person):
    def show(self):
        print("Student")


class Worker(Person):
    def show(self):
        print("Worker")


class WorkingStudent(Student, Worker):
    pass


w = WorkingStudent()
w.show()

class Device:
    def start(self):
        print("Device starts")


class Computer(Device):
    def start(self):
        print("Computer starts")


class Printer(Device):
    def start(self):
        print("Printer starts")


class AllInOne(Computer, Printer):
    pass


a = AllInOne()
a.start()