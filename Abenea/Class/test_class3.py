#!/usr/bin/env python

import inspect
import functools

class Person:
    """class containing info about a person"""

    def __init__(self, name):
        self.name = name


    def full_name(self):
        """get full name of a person"""
        return self.name

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<Person: {0}>'.format(self.name)

@functools.total_ordering
class Employee(Person):
    """inherits from CP"""
    def __init__(self, name, title, salary):
        Person.__init__(self, name)
        self.title = title
        self.salary = salary

    # to use functools.total_ordering, a class must provide __lt__ and __eq__
    def __lt__(self, other):
        """salary, position, name"""
        if self.salary < other.salary:
            return True
        elif self.salary > other.salary:
            return False

        # equal salaries
        if self.title.lower() < other.title.lower():
            return True
        elif self.title.lower() > other.title.lower():
            return False

        # equal positions
        if self.name.lower() < other.name.lower():
            return True
        elif self.name.lower() > other.name.lower():
            return False

        # equal names, too
        return False
        
    def __eq__(self, other):
        """salary, position, name"""
        return self.salary == other.salary and self.title.lower() == other.title.lower() and self.name.lower() == other.name.lower()
  
def test_employee():
      
    a = Person('A B')
    print str(a)
    print repr(a)


    tb = Employee('Thomas Brin', 'CEO', 500)
    js = Employee('John Smith', 'Engineer', 200)
    jd = Employee('John Doe', 'Engineer', 200)
    ba = Employee('Bryan Adams', 'Contractor', 200)

    assert tb == tb
    assert tb >= tb
    assert tb != js

    assert js > jd
    assert tb > js
    assert js >= jd
    assert tb >= js

    assert jd < js
    assert js < tb
    assert jd <= js
    assert js <= tb

    assert sorted([tb, js, jd, ba]) == [ba, jd, js, tb]


if __name__ == '__main__':

    test_employee()

