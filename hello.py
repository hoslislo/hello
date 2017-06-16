#!/usr/bin/env python

# import modules used here -- sys is a very standard one
import sys
import os

# Defines a "repeat" function that takes 2 arguments.
def repeat(s, exclaim):
    """
    Returns the string 's' repeated 3 times.
    If exclaim is true, add exclamation marks.
    """

    result = s + s + s  # can also use "s * 3" which is faster (Why?)
    if exclaim:
        result = result + '!!!' + '\n'
    else:
        result = result + '\n'
    return result


def main():
    print repeat('Yay', False)  ## YayYayYay
    print repeat('Woo Hoo', True)  ## Woo HooWoo HooWoo Hoo!!!
    print "done"

    #added a change ###try  toupload to git

    f = open("testio.txt",'r')
    for line in f:
        print(line)

    print "path   ", os.path.abspath(__file__)


'''
    try:
        f = open("C:Users\harry\PycharmProjects\testpath.txt",  'w')
        # perform file operations
        f.write( repeat('Yay', False))  ## YayYayYay
        f.write(repeat('Woo Hoo', True))  ## Woo HooWoo HooWoo Hoo!!!
        f.write("done")
    finally:
        f.close()

'''

if __name__ == "__main__":
    main()
