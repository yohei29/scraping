import sys
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui  import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import  Keys


URL = 'https://note.mu/'

def main():
    o = Options()
    o.add_argument('--headless')
    d = webdriver.Chrome(chrome_options=o)
    d.set_window_size(1200, 600)

    # d.save_screenshot('check.png')

    navigate(d)
    posts = scrape_post(d)

    for post in posts:
        print(post)
    print(len(posts))

def scrape_post(d):
    posts = []
    for a in d.find_elements_by_css_selector('.c-card'):
        posts.append({
            'url' : a.find_element_by_css_selector('a.c-card__link').get_attribute('href'),
            'title': a.find_element_by_css_selector('h3.p-cardItem__title').text,
            'description': a.find_element_by_css_selector('p').text,
        })
    return posts

def navigate(d):
    print('Navigate...', file=sys.stderr)
    d.get(URL)
    assert 'note' in d.title
    d.save_screenshot('check.png')
    wait = WebDriverWait(d, 10)

    print('Waiting for contents to loaded...', file=sys.stderr)
    d.execute_script('scroll(0, document.body.scrollHeight)')
    print('------')
    d.save_screenshot('check1.png')
    wait.until(EC.presence_of_element_located((By.ID, 'loading-bar-spinner')))
    wait.until(EC.invisibility_of_element_located((By.ID, 'loading-bar-spinner')))
    print('ok')
    d.save_screenshot('check2.png')

    print('Waitinf for contents to be loaded...', file=sys.stderr)

    d.execute_script('scroll(0, document.body.scrollHeight)')
    d.save_screenshot('check3.png')
    wait.until(EC.presence_of_element_located((By.ID, 'loading-bar-spinner')))
    wait.until(EC.invisibility_of_element_located((By.ID, 'loading-bar-spinner')))
    d.save_screenshot('check4.png')

    # print('Waiting for the more button to be clickble...', file=sys.stderr)
    # wait = WebDriverWait(d, 10)
    # res = wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, 'spinner-icon')))
    # time.sleep(2)
    # d.save_screenshot('check2.png')
    # # res = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'p-globalNavigation__item')))


if __name__ == '__main__':
    main()