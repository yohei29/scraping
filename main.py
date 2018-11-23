from settings import cmn
import requests
from bs4 import BeautifulSoup


# セッションを開始
session = requests.session()

# ログイン
login_info = {
    "login_field":'yohei29',
    "password":'yohan484803',
}

# action
url_login = "https://github.com/session"
res = session.post(url_login, data=login_info)
res.raise_for_status() # エラーならここで例外を発生させる

print(res.text)