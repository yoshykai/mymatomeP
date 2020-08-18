from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_binary
import time
from bs4 import BeautifulSoup
import urllib.request

file = open("list.csv")
wtxt = open("circled-me.csv",mode='w')
line = file.readlines()
file.close()
texts = []
name = []
for i in line:
    k = i.split(",")
    k[1] = k[1][:-1]
    name.append(k[0])
    texts.append(k[1])

URL = "https://meikasai.com/list.php"
driver = webdriver.Chrome()
driver.get(URL)
tableElem = driver.find_element_by_css_selector("table")
trs = tableElem.find_elements(By.TAG_NAME, "tr")
qqqq = 0
for i in trs:
    qqqq+=1
    if(qqqq==1):
        continue
    if(qqqq==20):
        print(tds[0].text)
        qqqq=1
    tds = i.find_elements(By.TAG_NAME, "td")
    if(tds[1].text in texts):
        q = texts.index(tds[1].text)
        wtxt.write(name[q]+","+tds[0].text[:1]+","+tds[0].text[1:3]+"\n")

driver.close()
driver.quit()
wtxt.close()
