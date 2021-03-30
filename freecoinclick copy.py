#!/usr/bin/python
# -*- coding:utf-8 -*-
from Tools import tools_v000 as tools
import os
import time
from os.path import dirname
import selenium
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger

# Mouse move
# https://automatetheboringstuff.com/chapter18/
import pyautogui
import pyperclip

# -13 for the name of this project FreeCoinClick
save_path = dirname(__file__)[ : -13]
propertiesFolder_path = save_path + "Properties"

# Example of used
# user_text = tools.readProperty(propertiesFolder_path, 'FreeCoinClick', 'user_text=')

dealy_properties = 30

def enterCredentials(url, user, password, X1, Y1, X2, Y2, Y3) :
#     tools.waitLoadingPageByXPATH2(dealy_properties, '/html/body/main/section/section[3]/div/div[3]/iframe')
#     iframe = tools.driver.find_element_by_xpath("/html/body/main/section/section[3]/div/div[3]/iframe")
#     iframe.
#     driver.switchTo().frame(driver.findElement(By.cssSelector("#generic-modal > iframe")));
# driver.findElement(By.id("close-button")).click();
# driver.switchTo().defaultContent();
    try :
        tools.driver.get(url)

        time.sleep(1)
        
        tools.waitLoadingPageByXPATH2(dealy_properties, '/html/body/main/section/section[1]/div/div/div[2]/div/div[1]/div[1]/input')
        username = tools.driver.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[1]/div[1]/input")
        username.send_keys(user)
        
        # Close the popup
        pyautogui.click(X1, Y1, button='left')

        time.sleep(1)

        # Go to the password
        pyautogui.click(X2, Y2, button='left')
        
        time.sleep(2)

        # pyautogui.click(X2, 515, button='left')
        for char in password:
            pyperclip.copy(char)
            # print(char)
            pyautogui.hotkey('ctrl', 'v', interval=0.1)

        time.sleep(1)

        # Click to ENTER
        pyautogui.click(X2, Y3, button='left')
        
        time.sleep(3)

        # test if the Countdown still visible
        tools.waitLoadingPageByXPATH2(dealy_properties, '/html/body/main/div/div/div/div/div/div[2]/div[1]')        
        tools.waitLoadingPageByXPATH2(dealy_properties, '/html/body/main/div/div/div/div/div/div[5]/button')
        rool = tools.driver.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button")
        while (True) : 
            # test = tools.driver.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[2]/div[1]")
            
            # 
            # # print (test.get_attribute("style"))
            # if (test.get_attribute("style") == "display: none;") :
            #     break
            # if (rool.get_attribute("style") != "display: none;") :
            #     break
            try :
                time.sleep(1)
                rool.click()
                break
            except selenium.common.exceptions.ElementNotInteractableException:
                print('Already run for this url ' + url) # Normally never append again with the test if the countdown still present
            
        
        time.sleep(10)
    except selenium.common.exceptions.NoSuchElementException:
        print('Error with this url : ' + url)
    except selenium.common.exceptions.UnexpectedAlertPresentException:
        print('Error with this url robot alert => skip : ' + url)

    # pyautogui.hotkey('command', 'w', interval=0.1)

    # tools.waitLoadingPageByXPATH2(dealy_properties, '/html/body/main/section/section[1]/div/div/div[2]/div/div[1]/div[2]/input')
    # password = tools.driver.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[1]/div[2]/input")
    # password.send_keys(password)

    # /html/body/main/section/section[1]/div/div/div[2]/div/div[1]/button
    # password.send_keys(Keys.ENTER)

def jobs() :
    # Open Browser
    tools.openBrowserBrave()

     # enterCredentials('https://freenem.com/free', 'pierre.thonon@gmail.com', '6^lqQs$82rPV', 750, 460, 850, 560, 650)

    enterCredentials('https://freedash.io/free', 'pierre.thonon@gmail.com', 'F0c2yC#naobb', 740, 500, 850, 530, 600)

    enterCredentials('https://freeethereum.com/free', 'pierre.thonon@gmail.com', '5o5ZDDWk#w%*', 740, 500, 850, 530, 600)

    enterCredentials('https://coinfaucet.io/free', 'pierre.thonon@gmail.com', 'Sck&H88WAvLB', 740, 500, 850, 560, 650)

    enterCredentials('https://freetether.com/free', 'pierre.thonon@gmail.com', 'XEwza2T&0cp^', 750, 460, 850, 530, 600)

    enterCredentials('https://freeusdcoin.com/free', 'pierre.thonon@gmail.com', 'XT^fm08&7Z$T', 740, 500, 850, 530, 600)

    enterCredentials('https://freesteam.io/free', 'pierre.thonon@gmail.com', '2#Kf0dt0Hxc7', 750, 460, 850, 530, 600)

    enterCredentials('https://freebitcoin.io/free', 'pierre.thonon@gmail.com', '83$DQyW6kM0r', 750, 460, 850, 510, 600)

    enterCredentials('https://free-tron.com/free', 'pierre.thonon@gmail.com', 'bNxQE74m@%My', 740, 500, 850, 530, 600)

    enterCredentials('https://freechainlink.io/free', 'pierre.thonon@gmail.com', '5j&WZ0AV0jS$', 740, 500, 850, 530, 600)

    enterCredentials('https://freeneo.io/free', 'pierre.thonon@gmail.com', '^3DCjZ0kk%3r', 750, 460, 850, 530, 600)

    enterCredentials('https://freecardano.com/free', 'pierre.thonon@gmail.com', '4z$x&L^8dMY2', 750, 460, 850, 630, 700)

    enterCredentials('https://freebinancecoin.com/free', 'pierre.thonon@gmail.com', '9rpE79Ca*Es8', 750, 460, 850, 530, 600)

    enterCredentials('https://free-doge.com/free', 'pierre.thonon@gmail.com', 'RkQ1$$VK1$fM', 750, 460, 850, 530, 600)


    print(str(datetime.now()))

    # Close Browser
    tools.closeBrowserChrome()

scheduler = BlockingScheduler()

# Schedules job_function to be run on the all minute
scheduler.add_job(jobs, 'cron', minute=(1))

scheduler.start()


# jobs()

# # Open BopenBrowserBrave()
# tools.openBrowserBrave()
# enterCredentials('https://freecardano.com/free', 'pierre.thonon@gmail.com', '4z$x&L^8dMY2', 750, 460, 850, 630, 700)