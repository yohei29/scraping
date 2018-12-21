from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import  Keys

o = Options()
o.add_argument('--headless')
d = webdriver.Chrome(chrome_options=o)
d.get('https://www.google.co.jp/')
assert 'Google' in d.title

input_ele = d.find_element_by_name('q')
input_ele.send_keys('Python')
input_ele.send_keys(Keys.ENTER)

assert 'Python' in d.title
# d.save_screenshot('s.png')

for a in d.find_elements_by_css_selector('.r'):
    # print(a.find_elements_by_css_selector('h3').text)
    print(a.find_element_by_css_selector('h3').text)
    print(a.find_element_by_css_selector('a').get_attribute('href'))
    print('----------------')