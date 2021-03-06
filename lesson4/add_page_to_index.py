__author__ = 'sebastian'

# Define a procedure, add_page_to_index,
# that takes three inputs:

# - index
#   - url (String)
#   - content (String)

# It should update the index to include
# all of the word occurences found in the
# page content by adding the url to the
# word's associated url list.

def lookup(index, keyword):
    for entry in index:
        if entry[0] == keyword:
            return entry[1]
    return []


def add_to_index(index, keyword, url):
    for entry in index:
        if entry[0] == keyword:
            entry[1].append(url)
            return
    index.append([keyword, [url]])
    return index


index = []


def add_page_to_index(index, url, content):
    content = content.split()
    for entry in content:
        add_to_index(index, entry, url)


add_page_to_index(index, 'fake.text', "This is a test")
print index
#>>> [['This', ['fake.text']], ['is', ['fake.text']], ['a', ['fake.text']],
#>>> ['test',['fake.text']]]



