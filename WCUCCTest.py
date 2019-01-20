from selenium import webdriver
# path="C:\\users\\ray\\appdata\\local\\programs\\python\\python36\\BrowsersDriver\\chromedriver.exe"
path="C:\\users\\ray\\appdata\\local\\programs\\python\\python36\\BrowsersDriver" # use for Firefox

# driver=webdriver.Chrome(path)
driver=webdriver.Firefox(path)
driver.get("https://www.myaccountaccess.com/onlineCard/login.do")
assert "Credit Card Account Access" in driver.title
# driver.close()
# driver.quit()
