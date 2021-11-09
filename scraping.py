# 以下コマンドをあらかじめ実行しインストール(anaconda環境なのでpython -m pip install seleniumを実行)
# python -m pip install selenium or pip3 install selenium or pip install selenium

# macなので以下コマンドを実行しfirefoxが制御できるようにする(chromedriverはエラーが出てうまくいかなかった)
# brew install geckodriver

# seleniumの読み込み
import selenium
from selenium import webdriver

# 一時停止用の標準ライブラリの読み込み
from time import sleep

browser = webdriver.Firefox()
browser.get('https://news.yahoo.co.jp/')

# 要素(element)を指定
#elem_username = browser.find_element_by_id('username')
# 文字を入力
# elem_username.send_keys('')
#elem_password = browser.find_element_by_id('')
# elem_password.send_keys('')
#elem_login_btn = browser.find_element_by_id('login-btn')
# elem_login_btn.click()

elem = browser.find_element_by_id('uamods-topics')
print(elem.text)

# browser.quit()
