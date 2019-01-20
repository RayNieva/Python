from selenium import webdriver
# path="C:\\users\\ray\\appdata\\local\\programs\\python\\python36\\BrowsersDriver\\chromedriver.exe"
path="C:\\users\\ray\\appdata\\local\\programs\\python\\python36\\BrowsersDriver" # use for Firefox

# driver=webdriver.Chrome(path)
driver=webdriver.Firefox(path)
driver.get("https://www.paypal.com/signin?country.x=US&locale.x=en_US")
assert "Log in to your PayPal account" in driver.title
# driver.close()
# driver.quit()
