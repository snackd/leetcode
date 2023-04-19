import requests
import json
from bs4 import BeautifulSoup
import csv
import pandas as pd
from openpyxl.workbook import Workbook

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

import configparser

session = requests.Session()

# 創建一個 ConfigParser 對象
config = configparser.ConfigParser()

config.read('config.ini')


# 動態 (selenium)
def selenium_crawler():
    options = Options()

    # 取消網頁中的彈出視窗
    options.add_argument("--disable-notifications")

    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    driver = webdriver.Chrome(options=options)

    # 使用瀏覽器訪問 Google 首頁
    driver.get("https://leetcode.com/accounts/login")

    user = driver.find_element(By.ID, "id_login")
    password = driver.find_element(By.ID, "id_password")

    user.send_keys("hidden")
    password.send_keys("hidden")

    signIn = driver.find_element(By.ID, "signin_btn")
    signIn.send_keys(Keys.ENTER)

    time.sleep(3)

    driver.get('https://leetcode.com/problemset/all/?status=AC&page=1')

    time.sleep(3)
    sElement = driver.find_element(By.CSS_SELECTOR, "[data-difficulty=TOTAL]")
    columns = sElement.text.split("\n")
    print(columns)

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    get_content(soup)

    # 關閉瀏覽器
    driver.close()


# 靜態 (requests)
def request_crawler():
    url = "https://leetcode.com/problemset/all"

    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")


def get_content(soup):
    problems = soup.find_all("div", attrs={"role": "rowgroup"})

    rows = problems[0].find_all("div", attrs={"role": "row"})

    df = pd.DataFrame(columns=['id', 'name', 'level'])
    i = 0
    for row in rows:
        # name = row.find(attrs={"class": "truncate"})
        name = row.find_all("div", attrs={"role": "cell"})[1].text

        level = row.find_all("div", attrs={"role": "cell"})[-2].text
        df.loc[i] = [name.split(".")[0], name, level]
        i += 1

    output(df)


def output(df):
    df.to_csv('leetcode.csv', index=False)
    df.to_excel('leetcode.xlsx', index=False)


def request_login():
    # 使用 session 建立一個連接
    session = requests.session()

    # 進行 Google 登入
    login_url = "https://leetcode.com/accounts/login"
    login_data = {
        "email": "hidden",
        "password": "hidden",
    }
    session.post(login_url, data=login_data)


def create_db():
    import sqlite3

    # 創建一個 SQLite 資料庫檔案
    conn = sqlite3.connect(config.get('info', 'db'))

    # 創建一個包含一個表格的資料庫
    cursor = conn.cursor()
    sql = ("CREATE TABLE leetcode "
           "(id INTEGER PRIMARY KEY, name TEXT, level TEXT)")
    cursor.execute(sql)
    conn.commit()

    # 關閉資料庫連線
    conn.close()


if __name__ == "__main__":
    # create_db()
    # crawler()
    selenium_crawler()
