#!/usr/bin/env python

import inspect

class Person:
    """class containing info about a person"""

    count = 0

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def full_name(self):
        """get full name of a person"""
        return self.fname + " " + self.lname

    def permissions(self):
        return "sleep, eat"

class Adult(Person):
    """class for adult"""
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)
        self.extra = "sex"

    def permissions(self):
        return Person.permissions(self) + ", " + self.extra
    
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
        return CountPerson.get_info(self) + " " + self.title + " "+ str(self.salary)



def test_employee():
    count = CountPerson.count
    
    a = CountPerson('A')
    assert a.get_info() == 'A'
    assert CountPerson.count == count + 1

    b = Employee('JS', 'Engineer', 200)
    
    print b.get_info()
    assert b.get_info() == 'JS Engineer 200'
    assert CountPerson.count == count + 2
    

if __name__ == '__main__':

    a = Adult('John', 'Doe')
    print "a.full_name: {0}".format(a.full_name())
    print "a.permissions: {0}".format(a.permissions())

    
    test_employee()

    cp = CountPerson("CP")

    print str(cp)
