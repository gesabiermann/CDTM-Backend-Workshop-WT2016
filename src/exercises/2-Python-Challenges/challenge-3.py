"""Classes and Functions:
1. Create a class that describes a person.
The person should have a name, an age, a study subject.
2. Add an initializer to this class, initializing the name, age and study properties
3. Add a method (function) that adds one year to the current age of the person.
4. Bonus: Define another class of your choice that is implemented by the class person"""
class Person():
    def __init__(self, name, age, study):
        self.name = name
        self.age = age
        self.study = study

    def agecalc(self, years):
        self.age = self.age + years

    def agecalc2(self):
        self.age = self.age + 2


def agecalc(person, years):
    person.age = person.age + years

person1 = Person("Tom", 22, "BWL")
print person1.name
agecalc(person1,1) # function
person1.agecalc(1) # method
person1.agecalc2()
print person1.age
