from settings import cmn

import requests
import os
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",
}

opt = Options()
opt.add_argument('__headless')
opt.add_argument('__disable-gpu')
drv = webdriver.Chrome(chrome_options=opt, executable_path=DRVPATH)

drv.get(cmn.URL)
source = drv.page_source
print(source)

# r = requests.post(URL, auth=(USER, PASS))
# r.encoding = r.apparent_encoding
# print(r.text)