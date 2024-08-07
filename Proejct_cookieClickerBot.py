from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import StaleElementReferenceException


# TODO MY def()
def upgrade_tool(money, price0, stores):
    if int(money.text.replace(',','')) >= price0:
        goodsName = stores_dict[price0]
        button = driver.find_element(By.ID, value=f'buy{goodsName}')  ## id="buyGrandma"
        try:
            button.click()
        except StaleElementReferenceException:  ##When you buy something, that part of the page (THE STORE PART) is refreshed and Selenium "loses" those elements. You'll have to find them again
            stores = driver.find_elements(By.CSS_SELECTOR, value='#store b')
        return stores


chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_option)
driver.get('https://orteil.dashnet.org/experiments/cookie/')


cookie = driver.find_element(By.ID, value='cookie')
stores = driver.find_elements(By.CSS_SELECTOR, value='#store b')

price_list =[]
stores_dict ={}
for item in stores:  #item.text: Cursor - 15
    list = item.text.split('-')
    try:
        price = list[1].replace(',', '').strip()
    except IndexError:
        pass
    else:
        stores_dict[int(price)] = list[0].strip()  # 如果用dict作为stores数据库：append to dict;
        price_list.append(int(price))  ## money

# print(f'price list = {price_list}') ## price list = [15, 100, 500, 2000, 7000, 50000, 1000000, 123456789]
# print(f'store dict = {stores_dict}') ## store dict = {15: 'Cursor', 100: 'Grandma', 500: 'Factory', 2000: 'Mine', 7000: 'Shipment', 50000: 'Alchemy lab', 1000000: 'Portal', 123456789: 'Time machine'}




#TODO 1 bot: to click on the cookie as fast as possible
#TODO 2 Every 5 seconds, check the right-hand pane to see which upgrades are affordable and purchase the most expensive one.
#TODO 3 After 5 minutes have passed since starting the game, stop the bot and print the "cookies/second"
time_start = time.time() ##by seconds; Old Start
timeout = 60*10 ## x min
round = 0

while time.time() < time_start+timeout: ## New End
    cookie.click()

    detalTime = int(time.time()) - int(time_start)
    if detalTime % 5 == 0: ## every 5 sec; int()因为浮点数太小，不加会错过
        money = driver.find_element(By.ID, value='money')  # check the money; default =2

        if detalTime <= 60:
            for price0 in reversed(price_list):
                stores = upgrad_tool(money, price0, stores)
        elif detalTime >60:
            for price0 in reversed(price_list[2:]):
                stores = upgrad_tool(money, price0, stores)
        elif detalTime > 300:
            for price0 in reversed(price_list[3:]):
                stores = upgrad_tool(money, price0, stores)
        elif detalTime > 500:
            for price0 in reversed(price_list[4:]):
                stores = upgrad_tool(money, price0, stores)
        else:
            for price0 in reversed(price_list[5:]):
                stores = upgrad_tool(money, price0, stores)


cookieSecond =driver.find_element(By.XPATH, value='//*[@id="cps"]')
print(cookieSecond.text)
money = driver.find_element(By.ID, value='money')  # check again the money
print(f'current cookie number is: {money.text}')


# driver.quit()


