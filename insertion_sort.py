#-------------------------------------------------------------------------------
# Name:        insertion sort
# Purpose:
#
# Author:      Florin
#
# Created:     31/03/2012
# Copyright:   (c) Florin 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def insertion_sort(a):
    """sort an array using insertion; time complexity O(n*n) """
    n = len(a)

    for i in range(1, n):
        #print ("i={0}".format(i))
        #print (a[j])
        key = a[i]
        j = i-1
        while (j>=0) and (a[j] > key):
            #print (j)
            #print (a[j])
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
        print (a)

    print (a)


def main():
    # initial array
    a = [31, 41, 59, 26, 41]
    print (a)

    insertion_sort(a)

if __name__ == '__main__':
    main()
