__author__ = 'Sebastian'
# Creating an Empty Hash Table
# Define a procedure, make_hashtable,
# that takes as input a number, nbuckets,
# and returns an empty hash table with
# nbuckets empty buckets.

def make_hashtable(nbuckets):
    hashtable = []
    counter = 0
    while counter < nbuckets:
        hashtable.append([])
        counter += 1
    return hashtable

print make_hashtable(5)

def hash_string(keyword,buckets):
    bucketsum = 0
    for e in keyword:
        bucketord = ord(e)
        bucketsum = bucketsum + bucketord
    bucketpos = bucketsum % buckets
    return bucketpos


