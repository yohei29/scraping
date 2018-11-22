from settings import cmn

import requests
import os
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",
}
print(cmn.PASS)

opt = Options()
# opt.set_headless(True)
# drv = webdriver.Chrome(chrome_options=opt, executable_path='C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')

# drv.get(URL)
# html = drv.get(URL)
# print(html)

# r = requests.post(URL, auth=(USER, PASS))
# r.encoding = r.apparent_encoding
# print(r.text)