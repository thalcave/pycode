#!/usr/bin/env python

import inspect

class Person:
    """class containing info about a person"""
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def full_name(self):
        """get full name of a person"""
        return self.fname + " " + self.lname

class Adult(Person):
    """class for adult"""
    sex = "allowed"
    
class CountPerson:
    """keeps track of how many objects were created"""

    count = 0
    def __init__(self, name):

        CountPerson.count += 1
        self.name = name

    def get_info(self):
        return self.name


class Employee(CountPerson):
    """inherits from CP"""
    def __init__(self, name, title, salary):
        CountPerson.__init__(self, name)
        self.title = title
        self.salary = salary

    def get_info(self):
        return CountPerson.get_info(self)

if __name__ == '__main__':
    print "main"

    setattr(Person, 'age', '27')

    print Person.__dict__
    print Person.__doc__
    print Person.__bases__



    jon = Person("Jon", "Bon Jovi")
    jon.age = 34
    print "jon age {0}".format(jon.__dict__['age'])
    print "jon.class {0}".format(jon.__class__)

    print "adult.bases: {0} adult dict:{1} adult.name: {2}".format(Adult.__bases__, Adult.__dict__, Adult.name)

    # will fail with "adult.name" key error
    # "name" doesn't belong to adult.__dict__
    #print "adult.name: ",Adult.__dict__['name']

    # Adult.name or getaddr(Adult, 'name') triggers attribute search
    print "adult.name: ",Adult.name,getattr(Adult, 'name')


    jon.fname ="Jon"
    jon.lname = "Bon Jovi"

    print "jon full name: ",jon.full_name()

    print "fname: ",jon.full_name,Person.full_name,jon.__init__

    print "adult method resolution order: ",inspect.getmro(Adult)



    count = CountPerson.count

    a = CountPerson('A')

    assert a.get_info() == 'A'


    b = CountPerson('B')

    print "counter: ",CountPerson.count


    b = Employee('J S', 'Engineer', 200)
    print "b: ",b.get_info()
