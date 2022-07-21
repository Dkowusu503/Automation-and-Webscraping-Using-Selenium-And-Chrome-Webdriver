import pandas as pd
import re
import selenium
import bs4
import lxml
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExpectedConditions
from selenium.common.exceptions import TimeoutException
import time

s = Service('C:\\Users\\dkowu\\Downloads\\chromedriver_win32\\chromedriver')
browser= webdriver.Chrome(service=s)
#browser.implicitly_wait(30)
browser.get("https://www.linkedin.com")
username= browser.find_element(By.ID, "session_key")
username.send_keys("dowusu@hawk.iit.edu")
password = browser.find_element(By.ID, "session_password")
password.send_keys("ENG28970")
wait=WebDriverWait(browser, 30)
#wait.until(ExpectedConditions.element_to_be_clickable((By.CLASS_NAME, "sign-in-form_submit-button")))
time.sleep(1)
#login_button = browser.find_element(By.CLASS_NAME, "sign-in-form_submit-button")
login_button = browser.find_element(By.CSS_SELECTOR, ".sign-in-form__submit-button")
login_button.click()
#browser.maximize_window()
browser.get("https://www.linkedin.com/jobs/search/?keywords=engineer")
browser.refresh()
time.sleep(75)
#Python code to find specific web elements By their ID's, Class name or CSS selector
job_title=browser.find_elements(By.CSS_SELECTOR, ".artdeco-entity-lockup--size-4 .artdeco-entity-lockup__title")
job_company=browser.find_elements(By.CSS_SELECTOR, ".artdeco-entity-lockup--size-4 .artdeco-entity-lockup__subtitle ")
job_location=browser.find_elements(By.CSS_SELECTOR, ".artdeco-entity-lockup--size-4 .artdeco-entity-lockup__caption")
job_benefits=browser.find_elements(By.CSS_SELECTOR,".artdeco-entity-lockup--size-4 .artdeco-entity-lockup__metadata")
#Misc=browser.find_elements(By.CSS_SELECTOR,".job-flavors__label")
a=[]
b=[]
c=[]
e=[]

for (i,j,k,l) in zip(job_title,job_company,job_location,job_benefits):
    time.sleep(60)
    a.append(i.text)
    b.append(j.text)
    c.append(k.text)
    e.append(l.text)

print(len(a))
browser.quit()
d={"Job Title":a,"Company":b,"Location":c,"Benefits":e}
df=pd.DataFrame(d)
#new = df["Location"].str.split("\n", n = 1, expand = True)
#df["Location1"]= new[0]
#df["Work Environment"]= new[1]
#df["State"]=new[2]
#df["Work Environment"]=new[3]
print(df.head())
#df.to_csv('C:\\Users\\dkowu\\Desktop\\Scraped Linkedin Engineer Jobs2022.csv')