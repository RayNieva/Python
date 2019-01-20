from selenium import webdriver
# path="C:\\users\\ray\\appdata\\local\\programs\\python\\python36\\BrowsersDriver\\chromedriver.exe"
path="C:\\users\\ray\\appdata\\local\\programs\\python\\python36\\BrowsersDriver" # use for Firefox

# driver=webdriver.Chrome(path)
driver=webdriver.Firefox(path)
driver.get("https://walmart.syf.com/eSecurity/Login/login.action?clientId=walmart&accountType=generic&langId=en")
assert "Manage Your Walmart Credit Card Account" in driver.title
# driver.close()
# driver.quit()
