#注意版本是4.2.2；老版本需要添加path等
from selenium import webdriver
from selenium.webdriver.common.by import By


# KEEP Chrome browser open after program finishes:
# --Chrome will automatically close the browser after opening (similar to Turtle or Tkinter)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)


# CREATE a Driver to "drive" the actions that will then occur on the browser-- options set above are passed in as well
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.python.org/')


# ELEMENT Locating
# date1 = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[1]/time') ##只能一个一个element找
# date11 = date1.text.split('T')[0]  ##2024-07-15

datetime = driver.find_elements(By.CSS_SELECTOR, value='.event-widget time')
datetime_list = [item.text for item in datetime]

event = driver.find_elements(By.CSS_SELECTOR, value='.event-widget a')
event_list = [item.text for item in event][1:] ##删除第一个more

events_dic = {datetime_list[i]:event_list[i] for i in range(len(event_list))}
## PRINT {'2024-07-15': 'Python Communities - University of Douala', '2024-07-17':...}
print(events_dic)



# CLOSE the tab/browser
# driver.close()  #close the tag
driver.quit()  #close the browser