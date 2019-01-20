from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# path="C:\\users\\ray\\appdata\\local\\programs\\python\\python36\\BrowsersDriver\\chromedriver.exe"
path="C:\\users\\ray\\appdata\\local\\programs\\python\\python36\\BrowsersDriver" # use for Firefox
user="raynieva@gmail.com"
pwd="p4raynieva"
# driver=webdriver.Chrome(path)
driver=webdriver.Firefox(path)
driver.get("https://www.facebook.com")
assert "Facebook" in driver.title
elem = driver.find_element_by_id("email")
elem.send_keys(user)
elem = driver.find_element_by_id("pass")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)
# driver.close()
