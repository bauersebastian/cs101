__author__ = 'Sebastian'
__author__ = 'Sebastian'

def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ""


def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote


def union(p, q):
    for e in q:
        if e not in p:
            p.append(e)


def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

def lookup(index, keyword):
    if keyword in index:
        return index[keyword]
    else:
        return None


def add_to_index(index, keyword, url):
    if keyword in index:
        index[keyword].append(url)
    else:
        index[keyword] = [url]

def record_user_click(index,keyword,url):


def add_page_to_index(index, url, content):
    content = content.split()
    for entry in content:
        add_to_index(index, entry, url)


def crawl_web(seed, max_pages):
    tocrawl = [seed]
    crawled = []
    index = {}
    while tocrawl and max_pages > len(crawled):
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index, page, content)
            union(tocrawl, get_all_links(content))
            crawled.append(page)
    return index

def split_string(source,splitlist):
    output = []
    atsplit = True
    for char in source:
        if char in splitlist:
            atsplit = True
        else:
            if atsplit:
                output.append(char)
                atsplit = False
            else:
                output[-1] = output[-1]+char
    return output

print crawl_web('http://www.udacity.com/cs101x/index.html', 1)
