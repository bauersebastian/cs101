__author__ = 'Sebastian'

# Define a function, hash_string,
# that takes as inputs a keyword
# (string) and a number of buckets,
# and returns a number representing
# the bucket for that keyword.

def hash_string(keyword,buckets):
    bucketsum = 0
    for e in keyword:
        bucketord = ord(e)
        bucketsum = bucketsum + bucketord
    bucketpos = bucketsum % buckets
    return bucketpos





print hash_string('a',12)
#>>> 1

print hash_string('b',12)
#>>> 2

print hash_string('a',13)
#>>> 6

print hash_string('au',12)
#>>> 10

print hash_string('udacity',12)
#>>> 11
