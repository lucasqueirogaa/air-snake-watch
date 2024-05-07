from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)

browser.get("https://google.com")

browser.find_element('xpath', '//*[@id="APjFqb"]').send_keys("Cotação Dolar")
browser.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]').click()
