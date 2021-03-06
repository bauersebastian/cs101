i = 0
while i<=10:
    print i
    i = i+1

z = 0
while z!=10:
    z = z+1
    print z

# Define a procedure, print_numbers, that takes
# as input a positive whole number, and prints
# out all the whole numbers from 1 to the input
# number.

# Make sure your procedure prints "upwards", so
# from 1 up to the input number.

def print_numbers(end_number):
    start_number = 1
    while start_number <= end_number:
        print start_number
        start_number = start_number+1

print print_numbers(50)

#print_numbers(3)
#>>> 1
#>>> 2
#>>> 3

# Define a procedure, factorial, that
# takes one number as its input
# and returns the factorial of
# that number.

def factorial(n):
    loops = 1
    result = n

    if n > 0:
        while loops < n:
            result = result * (n-loops)
            loops = loops + 1
        return result
    else:
        result = 1
    return result

print factorial(0)

def factsmart(u):
    resultus = 1
    while u >= 1:
        resultus = resultus * u
        u = u - 1
    return resultus

print factsmart(5)


#print factorial(4)
#>>> 24
#print factorial(5)
#>>> 120
#print factorial(6)
#>>> 720

def get_next_target(page):
    start_link = page.find('<a href=')

    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

url, endpos = get_next_target('good')
print url

if url:
    print "Here!"
else:
    print "Not here!"

def print_all_links(page):
    while True:
        url, endpos = get_next_target(page)
        if url:
            print url
            page = page[endpos:]
        else:
            break
