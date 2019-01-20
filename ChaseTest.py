from selenium import webdriver
# path="C:\\users\\ray\\appdata\\local\\programs\\python\\python36\\BrowsersDriver\\chromedriver.exe"
path="C:\\users\\ray\\appdata\\local\\programs\\python\\python36\\BrowsersDriver" # use for Firefox

# driver=webdriver.Chrome(path)
driver=webdriver.Firefox(path)
driver.get("https://www.chase.com/")
assert "Chase.com" in driver.title
# driver.close()
# driver.quit()
