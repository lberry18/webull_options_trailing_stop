#from multiprocessing.connection import wait
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

PATH = "C:\Program Files (x86)\Chromedriver.exe"
op = webdriver.ChromeOptions()
op.add_argument("user-data-dir=C:\\Users\\lando\\AppData\\Local\\Google\\Chrome\\User Data\\seleniumDriver")
ser = Service(PATH)
op.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=ser, options=op)

file = open("C:\\Users\lando\Documents\webull_script_login.txt", "r")
email = file.readline()
password = file.readline()
#print(email)


driver.get("https://app.webull.com/account")

driver.implicitly_wait(5)

unlock_acc = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div[1]/div/div/button')
unlock_acc.click()

input_1 = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[1]/div[2]/div[2]/div/input')
input_1.send_keys("0")

input_2 = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[1]/div[2]/div[2]/div/input')
input_2.send_keys("5")

input_3 = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[1]/div[2]/div[2]/div/input')
input_3.send_keys("3")

input_4 = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[1]/div[2]/div[2]/div/input')
input_4.send_keys("0")

input_5 = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[1]/div[2]/div[2]/div/input')
input_5.send_keys("9")

input_6 = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[1]/div[2]/div[2]/div/input')
input_6.send_keys("8")

trade_tab = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div[1]/div[6]/i')
trade_tab.click()

time.sleep(0.5)

open_contract = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div[1]/div/div[2]/div/div[1]/div[1]/div[3]/div/div/div/div[1]/table/tbody/tr/td[1]')
open_contract.click()

modify_contract = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div')
modify_contract.click()

#open_spy = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div[1]/div/div[2]/div/div[1]/div[2]/div[3]/div/div/div/div[1]/table/tbody/tr[1]/td[1]')
#open_spy.click()

#close_order = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div')
#close_order.click()

current_price = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div[1]/div/div[2]/div/div[1]/div[2]/div[3]/div/div/div/div[1]/table/tbody/tr[1]/td[6]')
current_price = float(current_price.text)
print(current_price)

stop_price = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div[1]/div/div[2]/div/div[1]/div[1]/div[3]/div/div/div/div[1]/table/tbody/tr/td[7]')
stop_price = float(stop_price.text)

last_price = current_price

calc = (last_price - current_price) / current_price * 100
print(calc)

#if current_price

#stop_price = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/div[2]/div[1]/div/div[3]/div[2]/div[1]/div[2]/div/input')))
update_price = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[2]/div[1]/div/div[3]/div[2]/div[1]/div[2]/div/input')
contract_price = float(update_price.get_attribute('value'))
print(contract_price)
time.sleep(0.1)
update_price.click()
update_price.send_keys(Keys.NUMPAD0)
update_price.send_keys(Keys.DECIMAL)
update_price.send_keys(Keys.NUMPAD0)
update_price.send_keys(Keys.NUMPAD7)


#auto stop loss and auto get out with win

#when i enter a trade automatically set my stop loss to $40 below what price i bought in on, for example if i get in at 1.50 per contract 1.10 would be my stop loss
#then make it auto exit if the price goes 70 above my stop loss, so if my stop is at 1.1 and the contract is up to 1.80 it automatically goes in and changes the stop loss to 5 below that price
