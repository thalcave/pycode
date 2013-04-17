#!/usr/bin/env python


class SimpleRange:
    def __init__(self, end):
        self.current = 0
        self.end = end

    def __iter__(self):
        return self

    def next(self):
        if self.current < self.end:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration


def test_range():
    for i in SimpleRange(3):
        print i
    assert list(SimpleRange(10)) == range(10)


if __name__ == '__main__':
    test_range()
