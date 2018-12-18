from robobrowser import RoboBrowser

URL = 'https://www.google.co.jp/'
SEARCH_CHAR = 'Python'

browser = RoboBrowser(parser='html.parser')
browser.open(URL)

form = browser.get_form(action='/search')
form['q'] = SEARCH_CHAR

browser.submit_form(form, list(form.submit_fields.values())[0])

for b in browser.select('h3 > a'):
    print(b.text)
    print(b.get('href'))