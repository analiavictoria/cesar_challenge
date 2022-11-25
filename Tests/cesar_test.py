from time import sleep
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = Firefox() 
driver.get("https://www.cesar.school/")

#Accepting cookies
cookies = driver.find_element(By.ID, 'onetrust-accept-btn-handler')
cookies.click()

#Menu navigation
hoverable = driver.find_element(By.XPATH, '/html/body/div[1]/header/div[2]/div/div/div/div[3]/div/nav/div/ul/li[1]/a/span[2]')
ActionChains(driver)\
    .move_to_element(hoverable)\
    .perform()

blog = driver.find_element(By.XPATH, '/html/body/div[1]/header/div[2]/div/div/div/div[3]/div/nav/div/ul/li[1]/ul/li[5]/a')
ActionChains(driver)\
    .move_to_element(blog)\
    .click()\
    .perform()

#Going to the secocnd page
sleep (5)
pagination = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/nav/div/a[1]')
pagination.click()

#Accessing articles

#3rd article: display title and publication date
sleep (5)
third_article = driver.find_element(By.ID, 'post-65915')
title = third_article.find_element(By.XPATH, '/html/body/div[1]/div/div/div/main/div/article[3]/div/div/header/h2/a')
print(title.text)

date = third_article.find_element(By.XPATH,'//*[@id="post-65937"]/div/div/div[1]/a/div/span/time[1]')
date_published = date.get_dom_attribute("datetime")
print(date_published)

#2nd article: exhibit author's name
second_article = driver.find_element(By.ID, 'post-65937')
author = second_article.find_element(By.CLASS_NAME,'author-name')
print(author.text)