from selenium import webdriver
# path="C:\\users\\ray\\appdata\\local\\programs\\python\\python36\\BrowsersDriver\\chromedriver.exe"
path="C:\\users\\ray\\appdata\\local\\programs\\python\\python36\\BrowsersDriver" # use for Firefox

# driver=webdriver.Chrome(path)
driver=webdriver.Firefox(path)
driver.get("https://citiretailservices.citibankonline.com/RSnextgen/svc/launch/index.action?siteId=PLOC_SHELL#signon")
assert "Shell Credit Card" in driver.title
# driver.close()
# driver.quit()
