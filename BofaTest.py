from selenium import webdriver
# path="C:\\users\\ray\\appdata\\local\\programs\\python\\python36\\BrowsersDriver\\chromedriver.exe"
path="C:\\users\\ray\\appdata\\local\\programs\\python\\python36\\BrowsersDriver" # use for Firefox

# driver=webdriver.Chrome(path)
driver=webdriver.Firefox(path)
driver.get("https://www.bankofamerica.com")
assert "Bank of America" in driver.title
#print("")
#input()

# driver.close()
# driver.quit()
