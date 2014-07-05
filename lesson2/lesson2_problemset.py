__author__ = 'Sebastian'

def udacify(inputstring):
    outputstring = "U"+inputstring
    return outputstring

print udacify('dacians')


def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(a,bigger(b,c))

def median(a,b,c):
     # swap the largest element into position "c" if necessary:
    if a > c:
        a,c = c,a
    if b > c:
        b,c = c,b
    # swap the second largest element into position "b" if necessary:
    if a > b:
        a,b = b,a
    # return the middle element:
    return b

print median(2,3,1)

# Define a procedure, countdown, that takes a
# positive whole number as its input, and prints
# out a countdown from that number to 1,
# followed by Blastoff!
# The procedure should not return anything.
# For this question, you just need to call
# the procedure using the line
# countdown(3)
# instead of print countdown(3).

def countdown(start):
    while start > 0:
        print start
        start = start-1
    print 'Blastoff!'

print countdown(5)

# Define a procedure, find_last, that takes as input
# two strings, a search string and a target string,
# and returns the last position in the search string
# where the target string appears, or -1 if there
# are no occurences.
#
# Example: find_last('aaaa', 'a') returns 3

# Make sure your procedure has a return statement.

def find_last(search, target):
    last_pos = -1
    while True:
        pos = search.find(target, last_pos+1)
        if pos == -1:
            return last_pos
        last_pos = pos

print find_last('baaa', 'a')

# 2 GOLD STARS

# Define a procedure, print_multiplication_table,
# that takes as input a positive whole number, and prints out a multiplication,
# table showing all the whole number multiplications up to and including the
# input number. The order in which the equations are printed matters.

# Hint: You can not add an integer and a string, but in homework 1.9
# you came across a method, str, for turning an integer into a string.

def print_multiplication_table(n):
    start = 1
    while start <= n:
        second = 1
        while second <= n:
            print str(start) + ' * '+ str(second)+' = '+ str(start*second)
            second = second + 1
        start = start + 1


print_multiplication_table(3)



def print_multiplication_table_for(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            print i, "*", j, "=", i*j

print_multiplication_table_for(3)
#>>> 1 * 1 = 1
#>>> 1 * 2 = 2
#>>> 2 * 1 = 2
#>>> 2 * 2 = 4

#print_multiplication_table(3)
#>>> 1 * 1 = 1
#>>> 1 * 2 = 2
#>>> 1 * 3 = 3
#>>> 2 * 1 = 2
#>>> 2 * 2 = 4
#>>> 2 * 3 = 6
#>>> 3 * 1 = 3
#>>> 3 * 2 = 6
#>>> 3 * 3 = 9
