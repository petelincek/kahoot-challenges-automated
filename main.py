from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import randrange
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(chrome_options=chrome_options)

PIN = "06711511"    #Pin of the game
NAME = "testing4" #Name of player (will be changed to array with more names in a loop to flood the room :)

time.sleep(2)
driver.get("https://kahoot.it/")
print(driver.title)
game_pin = driver.find_element_by_xpath('//*[@id="game-input"]')
game_pin.send_keys(PIN)
print("game_pin print")
enter = driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[2]/main/div/form/button')
enter.send_keys(Keys.RETURN)
print("enter pressed")
#Nickname input and confirmation
try:
    nickname = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="nickname"]'))
    )
    nickname.send_keys(NAME)
    nickname.send_keys(Keys.RETURN)
    print("nickname print")
    i = 1
    print(i)
    while True:
        try:
            ok_got_it = driver.find_element_by_xpath('//*[@id="core-modal-dialog"]/div/div[3]/button')
            ok_got_it.click()
            print("adding new nickname:")
            kak_dugi_name = len(NAME)
            print("Old name:")
            print(NAME)
            x = randrange(2)   #add rng number between 0 and 30 to the nickname
            nickname.send_keys(x)
            print("new name:")
            NAME = NAME + str(x)
            print(NAME)
            i = 2
            print(i)
            nickname.send_keys(Keys.RETURN)
        except:
            time.sleep(1)
        break
    
    if i == 2:
        try:
            ok_got_it = driver.find_element_by_xpath('//*[@id="core-modal-dialog"]/div/div[3]/button')
            ok_got_it.click()
            print("adding new nickname:")
            kak_dugi_name = len(NAME)
            print("Old name:")
            print(NAME)
            x = randrange(30)   #add rng number between 0 and 30 to the nickname
            nickname.send_keys(x)
            print("new name:")
            NAME = NAME + str(x)
            print(NAME)
            i = 1
            print(i)
        except:
            time.sleep(1)

    print(i)
    time.sleep(2)
    print("pressing Ok,go!")
    nickname.send_keys(Keys.RETURN)

finally:
   time.sleep(1)

print("waiting for animation to pass")
time.sleep(7) #animation time

#While loop for many questions
while True:
    try:    #anwser and next-button
        anwser = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="challenge-game-router"]/main/div[2]/div[1]'))
        )
        anwser.click()
        print("anwser print")
        time.sleep(3)
        next_button = driver.find_element_by_xpath('//*[@id="challenge-game-router"]/main/div[2]/div[3]/div/button')
        next_button.click()
        print("next_button print")
    finally:
       time.sleep(1)

    try:    #second next-button
        next_button_2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="challenge-game-router"]/div/main/div[2]/button'))
        )
        next_button_2.click()
        print("next_button_2 print")
        time.sleep(5)
    except:
        break
print("quiz finished!")
driver.quit()
