from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


chrome_driver_path = "/Users/lucassantos/Desktop/AA/A/DFSC/C/Work/Salles/CodeLive/CodeLive/usefull_projects/BotAva/chromedriver-mac-arm64/chromedriver"

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--user-data-dir=/Users/lucassantos/Library/Application Support/Google/Chrome")
options.add_argument("--profile-directory=Default")


driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

driver.get("https://ava.catolica.edu.br/d2l/lp/auth/saml/initiate-login?entityId=https://sts.windows.net/2009dfae-df11-49c7-804d-fda8d5cd9865/&target=%2fd2l%2fhome%2f6803")
time.sleep(10)


try:
    # Tentativa principal
    driver.find_element(By.XPATH, '//*[@id="idSIButton9"]').click()
    time.sleep(7)
    driver.find_element(By.XPATH, '//*[@id="idSIButton9"]').click()
    time.sleep(7)

except Exception as e1:
    print("Tentativa A falhou:", e1)
    try:
        # Tentativa alternativa (plano B)
        driver.find_element(By.XPATH, '//*[@id="idSIButton9"]').click()
        time.sleep(7)
        driver.find_element(By.XPATH, '//*[@id="idSIButton9"]').click()
        time.sleep(7)
        driver.find_element(By.XPATH, '//*[@id="idSIButton9"]').click()
        time.sleep(7)
    except Exception as e2:
        print("Tentativa B falhou também:", e2)

        # Plano C — última tentativa antes de desistir
        try:
            elemento = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
            elemento.click()
            time.sleep(1)
        except Exception as e3:
            print("Todas as tentativas falharam. Erro final:", e3)

driver.get("https://ava.catolica.edu.br/d2l/lp/auth/saml/initiate-login?entityId=https://sts.windows.net/2009dfae-df11-49c7-804d-fda8d5cd9865/&target=%2fd2l%2fhome%2f6803")
time.sleep(0.2)

course_links = [
    "https://ava.catolica.edu.br/d2l/home/103258",
    "https://ava.catolica.edu.br/d2l/le/content/103258/Home?itemIdentifier=D2L.LE.Content.ContentObject.ModuleCO-1774811",
    "https://ava.catolica.edu.br/d2l/home/103259",
    "https://ava.catolica.edu.br/d2l/le/content/103259/Home?itemIdentifier=D2L.LE.Content.ContentObject.ModuleCO-1775387",
    "https://ava.catolica.edu.br/d2l/home/103261",
    "https://ava.catolica.edu.br/d2l/le/content/103261/Home?itemIdentifier=D2L.LE.Content.ContentObject.ModuleCO-1775691",
    "https://ava.catolica.edu.br/d2l/home/103260",
    "https://ava.catolica.edu.br/d2l/le/content/103260/Home?itemIdentifier=D2L.LE.Content.ContentObject.ModuleCO-1775995",
    "https://ava.catolica.edu.br/d2l/home/103257",
    "https://ava.catolica.edu.br/d2l/le/content/103257/Home?itemIdentifier=D2L.LE.Content.ContentObject.ModuleCO-1775051"
]

for link in course_links:
    driver.get(link)
    time.sleep(7)