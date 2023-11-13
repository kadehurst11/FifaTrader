from tkinter import FALSE
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
import time
#buy_button_xpath = "/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/button[2]"
#request_headers = {"Host": "utas.mob.v1.fut.ea.com", "Sec-Ch-Ua": "'Not;A=Brand';v='99', 'Chromium';v='106'", "X-Ut-Sid": "7c0e3052-286a-4c65-9872-4c7d846da5d1", "Cache-Control": "no-cache", "Content-Type": "application/json", "Sec-C-Ua-Mobile": "?0", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.62 Safari/537.36", "Sec-Ua-Ch-Platform": "'macOS'", "Accept": "*/*", "Origin": "https://www.ea.com", "Sec-Fetch-Site": "same-site", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://www.ea.com/", "Accept-Encoding": "gzip, deflate", "Accept-Langauge": "en-US,en;q=0.9", "Connection": "close" }

def login(email, password, url):
        opts = webdriver.ChromeOptions()
        opts.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)" 
        +"AppleWebKit/537.36(KHTML, like Gecko)"
        +"Chrome/50.0.2661.102 Safari/537.36")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=opts)
        driver.get(url)
        time.sleep(10)
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "Login")))
            loginframe = driver.find_element(By.ID, "Login")
            utcontent = loginframe.find_element(By.CLASS_NAME,"ut-content")
            logincontent = utcontent.find_element(By.CLASS_NAME,"ut-login-content")
            logincontent.find_element(By.XPATH,"//*[@id='Login']/div/div/button[1]").click()
        except TimeoutException:
                print("LOADING TOOK TOO MUCH TIME")
        try:
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "login-form")))
                ealoginform = driver.find_element(By.ID, "login-form")
                ealoginform.find_element(By.ID, "email").send_keys(email)
                ealoginform.find_element(By.ID, "password").send_keys(password)
                ealoginform.find_element(By.XPATH, "//*[@id='login-form']/div[6]/span/label").click()
                ealoginform.find_element(By.XPATH, "//*[@id='logInBtn']").click()
        except TimeoutException:
                print("LOADING TOOK TOO MUCH TIME")
        try:
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "tfa-login")))
                tfalogin = driver.find_element(By.ID, "tfa-login")
                tfalogin.find_element(By.XPATH, "//*[@id='btnSendCode']").click()
                otc = input("Enter the OTC found in your email: ")
                tfa2login = driver.find_element(By.ID, "loginForm")
                tfa2login.find_element(By.ID, "twoFactorCode").send_keys(otc)
                tfa2login.find_element(By.XPATH, "//*[@id='verificationGate']/span/label").click()
                tfa2login.find_element(By.XPATH, "//*[@id='btnSubmit']").click()
        except TimeoutException:
                print("LOADING TOOK TOO MUCH TIME")
        return driver

def set_filter(driver):
        time.sleep(10)
        chem_styles = ["BASIC", "SNIPER", "FINISHER", "DEADEYE", "MARKSMAN", "HAWK", "ARTIST", "ARCHITECT", "POWERHOUSE", "MAESTRO", "ENGINE", "SENTINEL", "GUARDIAN", "GLADIATOR", "BACKBONE", "ANCHOR", "HUNTER", "CATALYST", "SHADOW", "WALL", "SHIELD", "CAT", "GLOVE", "GK BASIC", "None"]
        quality_types = ["FUT Heroes", "Icon", "Ones to Watch", "RULEBREAKERS", "Team of the Week", "UCL Road to the Knockouts", "UECL Road to the Knockouts", "UEFA Champions League Road to the Final", "UEFA Europa League Road to the Final", "UEL Road to the Knockouts", "Common", "Rare", "None"]
        try:
                WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "/html/body/main/section/nav/button[3]")))
                driver.find_element(By.XPATH, "/html/body/main/section/nav/button[3]").click()
        except TimeoutException:
                print("LOADING TOOK TOO MUCH TIME")
        try:
                WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,"/html/body/main/section/section/div[2]/div/div/div[2]")))
                driver.find_element(By.XPATH, "/html/body/main/section/section/div[2]/div/div/div[2]").click()
        except TimeoutException:
                print("LOADING TOOK TOO MUCH TIME")
        quality_list = driver.find_element(By.XPATH, "/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div/ul")
        qualities = quality_list.find_elements(By.TAG_NAME, "li").text
        print(qualities)
        positions = ["Defenders", "Midfielders", "Attackers", "GK", "RWB", "RB", "CB", "LB", "LWB", "CDM", "RM", "CM", "LM", "CAM", "CF", "RW", "ST", "LW", "None"]
        nationalities = ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua B.", "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "Belarus", "Belgium", "Benin", "Bermuda", "Bolivia", "Bosnia-H.", "Brazil", "Bulgaria", "Burk. Faso", "Burundi", "Cameroon", "Canada", "Cape Verde", "CAR", "Chad", "Chile", "China PR", "Chinese Taipei", "Colombia", "Comoros", "Congo", "Costa Rica", "Croatia", "Cuba", "Cyprus", "Czech Rep.", "Denmark", "Dom. Rep.", "DR Congo", "E. Guinea", "Ecuador", "Egypt", "El Salvad.", "England", "Estonia", "Ethiopia", "Faroe Isl.", "Fiji", "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Gibraltar", "Greece", "Grenada", "Guam", "Guatemala", "Guinea", "Guinea-Bis", "Guyana", "Haiti", "Honduras", "Hong Kong", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Isreal", "Italy", "Ivory Coast", "Jamaica", "Japan", "Kazakhstan", "Kenya", "Korea DPR", "Korea Rep.", "Kosovo", "Latvia", "Lebanon", "Liberia", "Libya", "Liechten", "Lithuania", "Luxemborg", "Macedonia", "Madagascar", "Malaysia", "Mali", "Malta", "Mauritania", "Mauritius", "Mexico", "Moldova", "Montenegro", "Montserrat", "Morocco", "Mozambique", "N. Ireland", "N.Antilles", "Nambia", "Netherlands", "New Zealand", "Nigeria", "Norway", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Puerto Rico", "Romania", "Russia", "S. Africa", "Saudi Ara.", "Scotland", "Serbia", "Sierra L.", "Singapore", "Slovakia", "Slovenia", "South Sudan", "Spain", "St Kitts Nevis", "St Lucia", "Sudan", "Suriname", "Sweden", "Switzerl.", "Syria", "Tanzania", "Thailand", "Togo", "Trinidad", "Tunisia", "Turkey", "Uganda", "Ukraine", "United Arab Emirates", "Uraguay", "USA", "Uzbekistan", "Venezuela", "Wales", "Zambia", "Zimbabwe", "None"]
        leagues = ["Premier League (ENG1)", "EFL Championship (ENG 2)", "EFL League One (ENG 3)", "EFL League Two (ENG 4)", "Ligue 1 Uber Eats (FRA 1)", "Ligue 2 BKT (FRA 2)", "Serie A TIM (ITA 1)", "Serie BKT (ITA 2)", "Bundesliga (GER 1)", "Bundesliga 2 (GER 2)", "3. Liga (GER 3)", "LaLiga Santander (ESP 1)", "LaLiga SmartBank (ESP 2)", "1A Pro League (BEL 1)", "3F Superliga (DEN 1)", "A-League (AUS 1)", "Allsvenskan (SWE 1)", "cinch Prem (SPFL)", "CSL (CHN 1)", "CSSL (SUI 1)", "Eliteserien (NOR 1)", "England Div. 5 (ENG 5)", "Eridivise (NED 1)", "Finnliiga (FIN 1)", "Hellaa Liga (GRE 1)", "Hero ISL (IND 1)", "Icons (ICN)", "K League 1 (KOR 1)", "Libertadores (LIB)", "Liga Colombia (COL 1)", "Liga Cyprus (CYP 1)", "Liga Hrvatska (CRO 1)", "Liga Portugal (POR 1)", "LPF (ARG 1)", "Magyar Liga (HUN 1)", "MBS Pro League (SAU 1)", "Men's National (INT)", "MLS (MLS)", "PKO Ekstraklasa (POL 1)", "South African FL (RSA 1)", "Special League (Special League)", "SSE Airtricity PD (IRL 1)", "Sudamericana (SUD)", "Süper Lig (TUR 1)", "SUPERLIGA (ROM 1)", "Ukrayina Liha (UKR 1)", "United Emirates League (UAE 1)", "Ö. Bundesliga", "Česká Liga (CZE 1)", "None"]
        delay = 2
        filter = {"Player Name": "", "Quality": "", "Rarity": "", "Position": "", "Chemistry Style": "", "Nationality": "", "League": "", "Club": "", "Max Price": "0"}
        driver.find_element(By.XPATH, "/html/body/main/section/nav/button[3]").click()
        try:
                WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/main/section/section/div[2]/div/div/div[2]")))
                driver.find_element(By.XPATH, "/html/body/main/section/section/div[2]/div/div/div[2]").click()
        except TimeoutException:
                print("LOADING TOOK TOO MUCH TIME")
        player_name = input("What player would you like to trade with? (If none just press enter)")
        filter["Player Name"] = player_name
        quality = ''

        input_message = "Which quality would you like to trade with? (If none type 'None')\n"

        for index, item in enumerate(qualities):
                input_message += f'{index+1}) {item}\n'

        input_message += 'Your choice: '

        while quality not in qualities:
                quality = input(input_message)

        filter["Quality"] = quality

        quality_type = ''

        input_message = "Which quality would you like to trade with? (If none type 'None')\n"

        for index, item in enumerate(quality_types):
                input_message += f'{index+1}) {item}\n'

        input_message += 'Your choice: '

        while quality_type not in quality_types:
                quality_type = input(input_message)
        filter["Rarity"] = quality_type

        position = ''

        input_message = "Which quality would you like to trade with? (If none type 'None')\n"

        for index, item in enumerate(positions):
                input_message += f'{index+1}) {item}\n'

        input_message += 'Your choice: '

        while position not in positions:
                position = input(input_message)
        filter["Position"] = position
        chem_style = ''

        input_message = "Which quality would you like to trade with? (If none type 'None')\n"

        for index, item in enumerate(chem_styles):
                input_message += f'{index+1}) {item}\n'

        input_message += 'Your choice: '

        while chem_style not in chem_styles:
                chem_style = input(input_message)
        filter["Chemistry Style"] = chem_style
        nation = ''

        input_message = "Which quality would you like to trade with? (If none type 'None')\n"

        for index, item in enumerate(nationalities):
                input_message += f'{index+1}) {item}\n'

        input_message += 'Your choice: '

        while nation not in nationalities:
                nation = input(input_message)
        filter["Nationality"] = nation
        league = ''

        input_message = "Which quality would you like to trade with? (If none type 'None')\n"

        for index, item in enumerate(leagues):
                input_message += f'{index+1}) {item}\n'

        input_message += 'Your choice: '

        while league not in leagues:
                league = input(input_message)
        filter["League"] = league
        for filtername, filtervalue in filter.items():
                #print(filtername, filtervalue)
                if(filtervalue == "" or filtervalue == "None"):
                        print("")
                else:
                        filters = driver.find_elements(By.CLASS_NAME, "label")
                        special = False
                        for i in range (0,len(filters)):
                                if(filtername.upper() == filters[i].text): 
                                        filters[i].click()
                                        time.sleep(1)
                                        inline_container = filters[i].find_element(By.XPATH, "../..")
                                        inline_list = inline_container.find_element(By.CLASS_NAME, "inline-list")
                                        inline_list_options = inline_list.find_elements(By.CLASS_NAME, "with-icon")
                                        print(len(inline_list_options))
                                        for i in range (0,len(inline_list_options)):
                                                if(inline_list_options[i].text == filtervalue):
                                                        inline_list_options[i].click()
                                                        break
                        max_price = input("What would be the highest you would like to pay for a player?")
                        driver.find_element(By.XPATH, "/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[6]/div[2]/input").send_keys(max_price)
                                        # if(i == 0):                            
                                        #         driver.find_element(By.XPATH, "/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div").click()
                                        #         inline_list = driver.find_element(By.XPATH, "/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div/ul")
                                        #         qualities = inline_list.find_elements(By.CLASS_NAME, "with-icon")
                                        #         for i in range (0,len(qualities)):
                                        #                 if(qualities[i].text == filtervalue):
                                        #                         qualities[i].click()
                                        # elif(i==1):
                                        #         driver.find_element(By.XPATH, f"/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[{i+1}]/div").click()
                                        #         inline_list = driver.find_element(By.XPATH, f"/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[{i+1}]/div/ul")
                                        #         rarities = inline_list.find_elements(By.CLASS_NAME, "with-icon")
                                        #         for i in range (0,len(rarities)):
                                        #                 if(rarities[i].text == filtervalue):
                                        #                         rarities[i].click()




                
def trade_with_filter(driver):
        delay = 2
        count = 0
        while(count < 10000):
                time.sleep(2)
                if(count%2 == 0):
                        max_price = max_price-50
                        search = driver.find_element(By.XPATH, "/html/body/main/section/section/div[2]/div/div[2]/div/div[2]/button[2]").click()
                        try:
                                no_players_img = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/main/section/section/div[2]/div/div/div[2]")))
                                if(no_players_img):
                                        driver.find_element(By.XPATH, "/html/body/main/section/section/div[1]/button[1]").click()
                                else:
                                        players = driver.find_elements(By.CLASS_NAME, "listFUTItem")
                                        for i in range(1,len(players)+1):
                                                driver.find_element(By.XPATH, f"/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li[{i}]").click()
                                                driver.find_element(By.XPATH, "/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/button[2]").click()
                                                driver.find_element(By.XPATH, "/html/body/div[4]/section/div/div/button[1]")
                        except TimeoutException:
                                print("LOADING TOOK TOO MUCH TIME")
                if(count%2 == 1):
                        max_price = max_price+50
                        search = driver.find_element(By.XPATH, "/html/body/main/section/section/div[2]/div/div[2]/div/div[2]/button[2]").click()
                        try:
                                players_check = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/main/section/section/div[2]/div/div/div[2]")))
                                if(players_check):
                                        driver.find_element(By.XPATH, "/html/body/main/section/section/div[1]/button[1]").click()
                                else:
                                        players = driver.find_elements(By.CLASS_NAME, "listFUTItem")
                                        for i in range(1,len(players)+1):
                                                driver.find_element(By.XPATH, f"/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li[{i}]").click()
                                                driver.find_element(By.XPATH, "/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/button[2]").click()
                                                driver.find_element(By.XPATH, "/html/body/div[4]/section/div/div/button[1]")
                        except TimeoutException:
                                print("LOADING TOOK TOO MUCH TIME")
email = "bllnkppp@outlook.com"
password = "Misskitty319"
driver = login(email,password,"https://www.ea.com/fifa/ultimate-team/web-app/")
set_filter(driver)
#trade_with_filter(driver)
