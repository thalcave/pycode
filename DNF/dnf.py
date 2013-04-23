#!/usr/bin/env python

""" Dutch National Flag problem:
The flag of the Netherlands consists of three colours: red, white and blue.
Given balls of these three colours arranged randomly in a line
(the actual number of balls does not matter),
the task is to arrange them such that all balls of the same colour
are together and their collective colour groups are in the correct order.
"""

import random

def sortArray(data):
    """sort an array containing (R,W,B) balls in order RWB"""

    idx = 0

    # keep an index for where the Blue zone starts
    blue_start = len(data) - 1

    # keep an index for where the Red zone ends
    red_end = -1

    idx = 0
    while idx < blue_start+1:
        #print data[idx]
        print data

        # if current ball is White, do nothing
        if data[idx] == "W":
            idx += 1
            continue

        # if current ball is Blue, move it to the end
        if data[idx] == "B":
            print "swap Blue %s,%s" % (idx,blue_start)

            # swap current ball with the start of Blue
            data[blue_start], data[idx] = data[idx], data[blue_start]

            # decrease the index for where the Blue zone starts
            blue_start -= 1
            continue

        # if current ball is Red, move it to Red zone
        red_end +=1
        if red_end != idx:
            print "swap Red %s,%s" % (idx,red_end)
            data[red_end], data[idx] = data[idx], data[red_end]

        idx += 1

        #swap element
        #data[idx], data[idx+1] = data[idx+1], data[idx]

def generateData():
    """generate an array of random length, containing R,W,B in random order"""

    # max length = 30
    while True:
        length = random.randrange(5, 30)
        if length:
            break

    print "length: ",length

    data = []

    colors = ['R', 'W', 'B']
    for x in range(0,length):
        data.append(random.choice(colors))

    return data


if __name__ == '__main__':
    data = generateData()
    #data = ['B', 'W', 'R', 'R', 'R', 'R']

    print "initial data: ",data

    sortArray(data)
    print "sorted  data: ",data



