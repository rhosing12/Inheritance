# ===============================
# 1. Single Inheritance
# ===============================
class Person:
    def __init__(self):
        pass

    def introduce(self):
        return "I am a person."


class Student(Person):
    def study(self):
        return "I am studying."


# ===============================
# 2. Multiple Inheritance
# ===============================
class Athlete:
    def __init__(self, sport):
        self.sport = sport


class Artist:
    def __init__(self, art_form):
        self.art_form = art_form


class MultiTalentedPerson(Athlete, Artist):
    def __init__(self, sport, art_form):
        Athlete.__init__(self, sport)
        Artist.__init__(self, art_form)

    def show_talents(self):
        return f"I play {self.sport} and practice {self.art_form}."


# ===============================
# 3. Multilevel Inheritance
# ===============================
class Employee:
    def work(self):
        return "I am working."


class Manager(Employee):
    def manage(self):
        return "I am managing a team."


class Director(Manager):
    def lead(self):
        return "I am leading the organization."


# ===============================
# 4. Hierarchical Inheritance
# ===============================
class Vehicle:
    def move(self):
        return "The vehicle is moving."


class Car(Vehicle):
    def drive(self):
        return "The car is being driven."


class Bike(Vehicle):
    def ride(self):
        return "The bike is being ridden."


# ===============================
# 5. Hybrid Inheritance (Multiple + Multilevel)
# ===============================
class Teacher(Person):
    def teach(self):
        return "I am teaching students."


class Researcher:
    def research(self):
        return "I am conducting research."


class Professor(Teacher, Researcher):
    def __init__(self):
        super().__init__()

    def role(self):
        return "I am a professor."


# ===============================
# Program Execution / Testing
# ===============================
# Single Inheritance
student = Student()
print(student.introduce())
print(student.study())

print("-" * 40)

# Multiple Inheritance
talented = MultiTalentedPerson("basketball", "painting")
print(talented.show_talents())

print("-" * 40)

# Multilevel Inheritance
director = Director()
print(director.work())
print(director.manage())
print(director.lead())

print("-" * 40)

# Hierarchical Inheritance
car = Car()
bike = Bike()
print(car.move())
print(car.drive())
print(bike.move())
print(bike.ride())

print("-" * 40)

# Hybrid Inheritance
professor = Professor()
print(professor.introduce())
print(professor.teach())
print(professor.research())
print(professor.role())
