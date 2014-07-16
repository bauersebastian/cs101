__author__ = 'sebastian'

# We defined:

stooges = ['Moe', 'Larry', 'Curly']

# but in some Stooges films, Curly was
# replaced by Shemp.

# Write one line of code that changes
# the value of stooges to be:

stooges[2] = 'Shemp'

print stooges

# ['Moe','Larry','Shemp']

# but does not create a new List
# object.

#Aliasing

# Define a procedure, replace_spy,
# that takes as its input a list of
# three numbers, and modifies the
# value of the third element in the
# input list to be one more than its
# previous value.

spy = [0, 0, 7]


def replace_spy(n):
    n[2] = n[2] + 1


# In the test below, the first line calls your
# procedure which will change spy, and the
# second checks you have changed it.
# Uncomment the top two lines below.

replace_spy(spy)
print spy
#>>> [0,0,8]

a = 3

# numbers or strings are not mutable in contrast to lists

def inc(n):
    n = n + 1
    return a, n


print inc(a)
