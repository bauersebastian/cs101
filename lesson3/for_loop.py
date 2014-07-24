__author__ = 'sebastian'

# Define a procedure, sum_list,
# that takes as its input a
# list of numbers, and returns
# the sum of all the elements in
# the input list.


def sum_list(numberlist):
    result = 0
    for element in numberlist:
        result = result + element
    return result


print sum_list([1, 7, 4])
# >>> 12

#print sum_list([9, 4, 10])
#>>> 23

#print sum_list([44, 14, 76])
#>>> 134


# Define a procedure, measure_udacity,
# that takes as its input a list of strings,
# and returns a number that is a count
# of the number of elements in the input
# list that start with the uppercase
# letter 'U'.

def measure_udacity(string_list):
    result = 0
    for element in string_list:
        search_string = element.find('U')
        if search_string == 0:
            result = result + 1
    return result


print measure_udacity(['Dave', 'Sebastian', 'Katy'])
#>>> 0

print measure_udacity(['Umika', 'Umberto'])
#>>> 2

# Define a procedure, find_element,
# that takes as its inputs a list
# and a value of any type, and
# returns the index of the first
# element in the input list that
# matches the value.

# If there is no matching element,
# return -1.

def find_element(input_list, target):
    count = 0
    for element in input_list:
        if element == target:
            return count
        count += 1
    return -1


#print find_element([1,2,3],3)
#>>> 2

#print find_element(['alpha','beta'],'gamma')
#>>> -1

# Define a procedure, find_element,
# using index that takes as its
# inputs a list and a value of any
# type, and returns the index of
# the first element in the input
# list that matches the value.

# If there is no matching element,
# return -1.

def find_elementindex(inlist, starget):
    if starget in inlist:
        resultc = inlist.index(starget)
        return resultc
    else:
        resultc = -1
        return resultc


print find_elementindex([1, 2, 3], 3)
#>>> 2

print find_elementindex(['alpha', 'beta'], 'gamma')
#>>> -1


