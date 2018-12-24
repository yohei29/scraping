import sys
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EX
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import feedgenerator

URL = 'https://note.mu/'
ENCODE = 'utf-8'

def main():
    o = Options()
    o.add_argument('--headless')
    d = webdriver.Chrome(chrome_options=o)
    d.set_window_size(1200, 600)

    nav(d)
    contents = get_contents(d)

    with open('recommend.rss', 'w', encoding=ENCODE) as f:
        save_rss(f, contents)

def save_rss(f, contents):
    feed = feedgenerator.Rss201rev2Feed(
        title='おすすめノート',
        link='https://note.mu/',
        description='おすすめノート'
    )

    for content in contents:
        feed.add_item(
            title=content['title'],
            link=content['url'],
            description=content['description'],
            unique_id=content['url'],
        )

    feed.write(f, ENCODE)

def nav(d):
    d.get(URL)
    assert 'note' in d.title

def get_contents(d):
    contents = []
    for a in d.find_elements_by_css_selector('.c-card'):
        contents.append({
            'url' : a.find_element_by_css_selector('a.c-card__link').get_attribute('href'),
            'title': a.find_element_by_css_selector('h3.p-cardItem__title').text,
            'description': a.find_element_by_css_selector('p').text,
        })
    return contents

if __name__ == '__main__':
    main()