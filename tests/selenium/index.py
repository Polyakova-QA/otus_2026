from selenium import webdriver
import time

chrome = webdriver.Chrome()
chrome.get('http://localhost:8081/')
print(chrome.title)
time.sleep(5)

chrome.quit()