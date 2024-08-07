from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_option)
driver.get('https://secure-retreat-92358.herokuapp.com/')


# #FIND AND CLICK the hyperlinked text
# # articleCount = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]')
# articleCount = driver.find_element(By.CSS_SELECTOR, value='#articlecount a')
# # print(articleCount.text)
# articleCount.clear()
#
# #FIND AND CLICK element by Link Text
# contentPortals = driver.find_element(By.LINK_TEXT, value='Content portals') #value = link text
# contentPortals.click()
#
# #FIND the 'Search'<input> by Name
# search = driver.find_element(By.NAME, value='search')
# #SENDING keyboard input to Selenium
# search.send_keys(" I'll search sth...", Keys.ENTER)


#TODO AUTO FILL-IN a SIGN-UP web form
first_name = driver.find_element(By.NAME, value='fName')
last_name = driver.find_element(By.NAME, value='lName')
email = driver.find_element(By.NAME, value='email')
signUpButton = driver.find_element(By.CSS_SELECTOR, value="form button")

first_name.send_keys('Ely')
last_name.send_keys('Panda')
email.send_keys('123456@163.com')
signUpButton.send_keys(Keys.ENTER)

driver.quit()
