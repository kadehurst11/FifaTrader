from tkinter import FALSE
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
import requests
from bs4 import BeautifulSoup
import time

def login(email, password, url):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(url)
        time.sleep(20)
        loginframe = driver.find_element(By.ID, "Login")
        utcontent = loginframe.find_element(By.CLASS_NAME,"ut-content")
        logincontent = utcontent.find_element(By.CLASS_NAME,"ut-login-content")
        logincontent.find_element(By.XPATH,"//*[@id='Login']/div/div/button[1]").click()
        time.sleep(20)
        ealoginform = driver.find_element(By.ID, "login-form")
        ealoginform.find_element(By.ID, "email").send_keys(email)
        ealoginform.find_element(By.ID, "password").send_keys(password)
        ealoginform.find_element(By.XPATH, "//*[@id='login-form']/div[6]/span/label").click()
        ealoginform.find_element(By.XPATH, "//*[@id='logInBtn']").click()
        time.sleep(10)
        tfalogin = driver.find_element(By.ID, "tfa-login")
        tfalogin.find_element(By.XPATH, "//*[@id='btnSendCode']").click()
        otc = input("Enter the OTC found in your email: ")
        tfa2login = driver.find_element(By.ID, "loginForm")
        tfa2login.find_element(By.ID, "twoFactorCode").send_keys(otc)
        tfa2login.find_element(By.XPATH, "//*[@id='verificationGate']/span/label").click()
        tfa2login.find_element(By.XPATH, "//*[@id='btnSubmit']").click()
        time.sleep(30)
        return driver

def getPrice(player_dict):
    delay = 2
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36(KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    sesh = requests.Session()
    url = f"https://www.futbin.com/players?page=1&search={player_dict['Name']}&Pace={player_dict['PAC']}, {player_dict['PAC']}&Shooting={player_dict['SHO']},{player_dict['SHO']}&pdribbling={player_dict['DRI']},{player_dict['DRI']}&Defending={player_dict['DEF']},{player_dict['DEF']}&Passing={player_dict['PAS']},{player_dict['PAS']}&Physicality={player_dict['PHY']},{player_dict['PHY']}"
    player_html = sesh.get(url, headers=headers).text
    soup = BeautifulSoup(player_html, 'html.parser')
    player_price = soup.select_one(".ps4_color.font-weight-bold").get_text(strip=True)
    return player_price

def sell(driver):
    delay = 2
    driver.find_element(By.XPATH, "/html/body/main/section/nav/button[3]").click()
    try:
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/main/section/section/div[2]/div/div/div[3]")))
        driver.find_element(By.XPATH, "/html/body/main/section/section/div[2]/div/div/div[3]").click()
    except TimeoutException:
        print("LOADING TOOK TOO MUCH TIME")
    players_on_transfer_list = driver.find_elements(By.CLASS_NAME, "listFUTItem")
    if(players_on_transfer_list):
        for player in players_on_transfer_list:
            player_dict = {}
            player_dict["Name"] = driver.find_element(By.XPATH, "/html/body/main/section/section/div[2]/div/div/div/section[3]/ul/li[1]/div/div[1]/div[2]").text
            print(player_dict["Name"])
            keys_values_list = player.find_element(By.XPATH, "/html/body/main/section/section/div[2]/div/div/div/section[3]/ul/li/div/div[1]/div[3]/ul")
            print(keys_values_list)
            keys_values = keys_values_list.find_elements(By.TAG_NAME, "li")
            print(keys_values)
            keys = keys_values.find_elements(By.CLASS_NAME, "label").text
            print(keys)
            values = keys_values.find_elements(By.CLASS_NAME, "value").text
            print(values)
            for key,value in zip(keys, values):
                player_dict[key] = value
            player_price = getPrice(player_dict)
            if((player_dict["Name"]) == driver.find_element(By.XPATH, "/html/body/main/section/section/div[2]/div/div/div/section[3]/ul/li[1]/div/div[1]/div[2]")):
                time.sleep(1)
                driver.find_element(By.XPATH, "/html/body/main/section/section/div[2]/div/div/section/div/div/div[2]/div[2]/div[1]/button").click()
                time.sleep(1)
                driver.find_element(By.XPATH, "/html/body/main/section/section/div[2]/div/div/section/div/div/div[2]/div[2]/div[2]/div[3]/div[2]/input").send_keys(player_price)
                time.sleep(1)
                driver.find_element(By.XPATH, "/html/body/main/section/section/div[2]/div/div/section/div/div/div[2]/div[2]/div[2]/div[2]/div[2]/input").send_keys(player_price-1)
                time.sleep(1)
                driver.find_element(By.XPATH, "/html/body/main/section/section/div[2]/div/div/section/div/div/div[2]/div[2]/div[2]/button").click()
    else:
        driver.navigate().refresh()
        sell(driver)
        
email = "bllnkppp@outlook.com"
passw = "Misskitty319"
player_dict = {}
driver = login(email, passw, "https://www.ea.com/fifa/ultimate-team/web-app/")
sell(driver)