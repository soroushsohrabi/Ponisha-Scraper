import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://ponisha.ir/")
inpts = driver.find_elements(By.CLASS_NAME, "MuiIconButton-root")
inpts[3].click()
time.sleep(2)
inpts = driver.find_elements(By.ID, "input-username")
inpts[0].send_keys("soroush.sohrabi50@gmail.com")
time.sleep(1)
inpts = driver.find_elements(By.CLASS_NAME, "MuiTypography-root")
inpts[2].click()
time.sleep(1)
inpts = driver.find_elements(By.ID, "input-password")
inpts[0].send_keys("272937042soroush")
time.sleep(1)
inpts = driver.find_elements(By.CLASS_NAME, "MuiButtonBase-root")
inpts[2].click()
time.sleep(1)
inpts = driver.find_elements(By.CLASS_NAME, "MuiTypography-root")
inpts[3].click()
time.sleep(10)
inpts = driver.find_elements(By.XPATH, '/html/body/div/div[1]/div[2]/div/div/div[2]/div[2]/div[2]/div/a/button')
time.sleep(7)
inpts[0].click()
time.sleep(10)
ads = driver.find_elements(By.CLASS_NAME, "css-fz2v58")

data=[]
for ad in ads:
    title = ad.find_elements(By.CLASS_NAME, "MuiTypography-h4")
    description = ad.find_elements(By.CLASS_NAME, "css-uo3dt4")
    skill = ad.find_elements(By.CLASS_NAME, "css-wgqnl1")
    price = ad.find_elements(By.CLASS_NAME, "css-ri6noj")
    data.append({
        "title": title[0].text,
        "description": description[0].text,
        "skill": skill[0].text,
        "price": price[2].text,
    })

js=json.dumps(data)
with open("ads.json","wt",encoding="utf-8") as f1:
    f1.write(js)