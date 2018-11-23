import lxml.html

ele = lxml.html.parse('index.html')

html = ele.getroot()

for v in html.cssselect('a'):
    print(v)