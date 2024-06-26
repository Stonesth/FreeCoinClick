#!/usr/bin/python
# -*- coding:utf-8 -*-
from Tools import tools_v000 as tools
import os
import time
import platform
from os.path import dirname
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

# Mouse move
# https://automatetheboringstuff.com/chapter18/
import pyautogui
import pyperclip

# -13 for the name of this project FreeCoinClick
save_path = dirname(__file__)[ : -13]
propertiesFolder_path = save_path + "Properties"

# Example of used
freenem = tools.readProperty(propertiesFolder_path, 'FreeCoinClick', 'freenem=')
freedash = tools.readProperty(propertiesFolder_path, 'FreeCoinClick', 'freedash=')
freeethereum = tools.readProperty(propertiesFolder_path, 'FreeCoinClick', 'freeethereum=')
coinfaucet = tools.readProperty(propertiesFolder_path, 'FreeCoinClick', 'coinfaucet=')
freetether = tools.readProperty(propertiesFolder_path, 'FreeCoinClick', 'freetether=')
freeusdcoin = tools.readProperty(propertiesFolder_path, 'FreeCoinClick', 'freeusdcoin=')
freesteam = tools.readProperty(propertiesFolder_path, 'FreeCoinClick', 'freesteam=')
freebitcoin = tools.readProperty(propertiesFolder_path, 'FreeCoinClick', 'freebitcoin=')
freetron = tools.readProperty(propertiesFolder_path, 'FreeCoinClick', 'freetron=')
freechainlink = tools.readProperty(propertiesFolder_path, 'FreeCoinClick', 'freechainlink=')
freeneo = tools.readProperty(propertiesFolder_path, 'FreeCoinClick', 'freeneo=')
freecardano = tools.readProperty(propertiesFolder_path, 'FreeCoinClick', 'freecardano=')
freebinancecoin = tools.readProperty(propertiesFolder_path, 'FreeCoinClick', 'freebinancecoin=')
freedoge = tools.readProperty(propertiesFolder_path, 'FreeCoinClick', 'freedoge=')

dealy_properties = 30
test = True

def enterCredentials(url, user, password, X1, Y1, X2, Y2, Y3) :
#     tools.waitLoadingPageByXPATH2(dealy_properties, '/html/body/main/section/section[3]/div/div[3]/iframe')
#     iframe = tools.driver.find_element_by_xpath("/html/body/main/section/section[3]/div/div[3]/iframe")
#     iframe.
#     driver.switchTo().frame(driver.findElement(By.cssSelector("#generic-modal > iframe")));
# driver.findElement(By.id("close-button")).click();
# driver.switchTo().defaultContent();
    # try :
    tools.openBrowserBrave()
    tools.driver.get(url)

    time.sleep(1)
    
    tools.waitLoadingPageByXPATH2(dealy_properties, '/html/body/main/section/section[1]/div/div/div[2]/div/div[1]/div[1]/input')
    username = tools.driver.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[1]/div[1]/input")
    username.send_keys(user)

    # Remove the blocker
    try :
        tools.driver.execute_script("""var l = document.getElementsByClassName("d-none d-lg-block")[0];l.parentNode.removeChild(l);""")
        time.sleep(1)
    except selenium.common.exceptions.JavascriptException:
        print('64 - javascript error: Invalid or unexpected token => skip : ' + url)
        pass

    try :
        tools.driver.execute_script("""var l = document.getElementById("zone-4545ff844213faef343;l.parentNode.removeChild(l);""")
        time.sleep(1)
    except selenium.common.exceptions.JavascriptException:
        print('71 - javascript error: Invalid or unexpected token => skip : ' + url)
        pass

    try :
        tools.driver.execute_script("""var l = document.getElementById("zone-2575f1dba0fa64ea629;l.parentNode.removeChild(l);""")
        time.sleep(1)
    except selenium.common.exceptions.JavascriptException:
        print('78 - javascript error: Invalid or unexpected token => skip : ' + url)
        pass

    try :
        tools.driver.execute_script("""var l = document.getElementByXPath("/html/body/a[1]/div;l.parentNode.removeChild(l);""")
        time.sleep(1)
    except selenium.common.exceptions.JavascriptException:
        print('85 - javascript error: Invalid or unexpected token => skip : ' + url)
        pass

    try :
        all_iframes = tools.driver.find_elements_by_tag_name("iframe")
        if len(all_iframes) > 0:
            print("Ad Found\n")
            tools.driver.execute_script("""
                var elems = document.getElementsByTagName("iframe"); 
                for(var i = 0, max = elems.length; i < max; i++)
                    {
                        elems[i].parentNode.removeChild(elems[i])
                    }
                                """)
            print('Total Ads: ' + str(len(all_iframes)))
        else:
            print('No frames found')
    except :
        print('ERROR')


    try :
        tools.driver.execute_script("""var l = document.getElementById("mPlbG9oKdeU3PaZkySdDX1n4dr8O9yZec;l.parentNode.removeChild(l);""")
        time.sleep(1)
    except selenium.common.exceptions.JavascriptException:
        print('78 - javascript error: Invalid or unexpected token => skip : ' + url)
        pass
    
    try :
        tools.driver.execute_script("""var l = document.getElementById("VSyPqy2vDXqoMQ4XhqYQS428naHW2HcBu;l.parentNode.removeChild(l);""")
        time.sleep(1)
    except selenium.common.exceptions.JavascriptException:
        print('78 - javascript error: Invalid or unexpected token => skip : ' + url)
        pass
    
    try :
        tools.driver.execute_script("""var l = document.getElementById("n6n6Zyiy4yqG5wrFqhRBCvxT3niLs1mED;l.parentNode.removeChild(l);""")
        time.sleep(1)
    except selenium.common.exceptions.JavascriptException:
        print('78 - javascript error: Invalid or unexpected token => skip : ' + url)
        pass

    

    # Copy the password
    tools.waitLoadingPageByXPATH2(dealy_properties, '/html/body/main/section/section[1]/div/div/div[2]/div/div[1]/div[2]/input')
    passw = tools.driver.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[1]/div[2]/input")
    passw.click()
    passw.send_keys(password)

    time.sleep(1)

    # # Close the popup
    # pyautogui.click(int(X1), int(Y1), button='left')

    # time.sleep(1)

    # # Go to the password
    # pyautogui.click(int(X2), int(Y2), button='left')

    # # Removed all the new tab if popup after go to the main page
    # driver_len = len(tools.driver.window_handles) #fetching the Number of Opened tabs
    # while (driver_len > 1) :
    #     # print("Length of Driver = ", driver_len)
    #     if driver_len > 1: # Will execute if more than 1 tabs found.
    #         for i in range(driver_len - 1, 0, -1):
    #             tools.driver.switch_to.window(tools.driver.window_handles[i]) #will close the last tab first.
    #             tools.driver.close()
    #             # print("Closed Tab No. ", i)
    #         tools.driver.switch_to.window(tools.driver.window_handles[0]) # Switching the driver focus to First tab.
    #         pyautogui.click(int(X2), int(Y2), button='left')
    #     else:
    #         print("Found only Single tab.")
    #     driver_len = len(tools.driver.window_handles) #fetching the Number of Opened tabs
    
    # time.sleep(2)

    # # Introduce the password with the command CTRL + V / Command + V
    # for char in password:
    #     pyperclip.copy(char)
    #     # print(char)
    #     if platform.system() == 'Darwin' :
    #         pyautogui.hotkey('command', 'v', interval=0.01)
    #     else :
    #         pyautogui.hotkey('ctrl', 'v', interval=0.01)

    # time.sleep(1)

    # Click to ENTER
    # pyautogui.click(int(X2), int(Y3), button='left')
    tools.waitLoadingPageByXPATH2(dealy_properties, "/html/body/main/section/section[1]/div/div/div[2]/div/div[1]/button")
    submit_button = tools.driver.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[1]/button")
    submit_button.click()
    
    time.sleep(1)

    if (test == False ) :
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
                time.sleep(20)

                break
            except selenium.common.exceptions.ElementNotInteractableException:
                print('Already run for this url ' + url) # Normally never append again with the test if the countdown still present
                break
            except selenium.common.exceptions.UnexpectedAlertPresentException:
                print('138 - Error with this url robot alert => skip : ' + url)

                if platform.system() == 'Darwin' :
                    pyautogui.hotkey('command', 'r')
                else :
                    pyautogui.hotkey('ctrl', 'r')
                continue
    else :
        print('168 : ' + url)
        while (True) :
            try :
                tools.waitLoadingPageByXPATH2(dealy_properties, '/html/body/main/div/div/div/div/div/div[5]/button')
                rool = tools.driver.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button")
                rool.click()

                time.sleep(10)

                print('177 : ' + url)
                tools.waitLoadingPageByXPATH2(dealy_properties, '/html/body/main/div/div/div/div/div/div[5]/button')
                rool = tools.driver.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button")

                print('181 : ' + url)

            except selenium.common.exceptions.ElementNotInteractableException:
                print('Already run for this url ' + url) # Normally never append again with the test if the countdown still present
                break
            except selenium.common.exceptions.UnexpectedAlertPresentException:
                print('138 - Error with this url robot alert => skip : ' + url)

                if platform.system() == 'Darwin' :
                    pyautogui.hotkey('command', 'r')
                else :
                    pyautogui.hotkey('ctrl', 'r')

                time.sleep(5)
                
                continue

        print('192 : ' + url)

        
    # except selenium.common.exceptions.NoSuchElementException:
    #     print('Error with this url : ' + url)
    # except selenium.common.exceptions.ElementNotInteractableException:
    #     print('Already run for this url ' + url) # Normally never append again with the test if the countdown still present
    
    #     # Try to refresh the page until past to the next step
        
    #     while (True) :
    #         print('Try to refresh the page ' + url)
    #         try : 
    #             if platform.system() == 'Darwin' :
    #                 pyautogui.hotkey('command', 'r')
    #             else :
    #                 pyautogui.hotkey('ctrl', 'r')
                
    #             time.sleep(1)
    #             rool = tools.driver.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button")
    #             rool.click()

    #             time.sleep(1)
    #             break
    #         except selenium.common.exceptions.UnexpectedAlertPresentException:
    #             print('164 - Error with this url robot alert => skip : ' + url)
    #             pass
            
    print('End of the process for the url : ' + url)
    tools.closeBrowserChrome()

    # pyautogui.hotkey('command', 'w', interval=0.1)

    # tools.waitLoadingPageByXPATH2(dealy_properties, '/html/body/main/section/section[1]/div/div/div[2]/div/div[1]/div[2]/input')
    # password = tools.driver.find_element_by_xpath("/html/body/main/section/section[1]/div/div/div[2]/div/div[1]/div[2]/input")
    # password.send_keys(password)

    # /html/body/main/section/section[1]/div/div/div[2]/div/div[1]/button
    # password.send_keys(Keys.ENTER)

def jobs() :
    # Open Browser
    print(str(datetime.now()))

    farray = freenem.split(", ")
    # enterCredentials(farray[0], farray[1], farray[2], farray[3], farray[4], farray[5], farray[6], farray[7])

    farray = freedash.split(", ")
    enterCredentials(farray[0], farray[1], farray[2], farray[3], farray[4], farray[5], farray[6], farray[7])
    
    farray = freeethereum.split(", ")
    enterCredentials(farray[0], farray[1], farray[2], farray[3], farray[4], farray[5], farray[6], farray[7])

    farray = coinfaucet.split(", ")
    enterCredentials(farray[0], farray[1], farray[2], farray[3], farray[4], farray[5], farray[6], farray[7])

    farray = freetether.split(", ")
    enterCredentials(farray[0], farray[1], farray[2], farray[3], farray[4], farray[5], farray[6], farray[7])

    farray = freeusdcoin.split(", ")
    enterCredentials(farray[0], farray[1], farray[2], farray[3], farray[4], farray[5], farray[6], farray[7])

    farray = freesteam.split(", ")
    enterCredentials(farray[0], farray[1], farray[2], farray[3], farray[4], farray[5], farray[6], farray[7])

    farray = freebitcoin.split(", ")
    enterCredentials(farray[0], farray[1], farray[2], farray[3], farray[4], farray[5], farray[6], farray[7])

    farray = freetron.split(", ")
    enterCredentials(farray[0], farray[1], farray[2], farray[3], farray[4], farray[5], farray[6], farray[7])

    farray = freechainlink.split(", ")
    enterCredentials(farray[0], farray[1], farray[2], farray[3], farray[4], farray[5], farray[6], farray[7])

    farray = freeneo.split(", ")
    enterCredentials(farray[0], farray[1], farray[2], farray[3], farray[4], farray[5], farray[6], farray[7])

    farray = freecardano.split(", ")
    enterCredentials(farray[0], farray[1], farray[2], farray[3], farray[4], farray[5], farray[6], farray[7])

    farray = freebinancecoin.split(", ")
    enterCredentials(farray[0], farray[1], farray[2], farray[3], farray[4], farray[5], farray[6], farray[7])

    farray = freedoge.split(", ")
    enterCredentials(farray[0], farray[1], farray[2], farray[3], farray[4], farray[5], farray[6], farray[7])

    print(str(datetime.now()))

    # Close Browser
    tools.driver.quit()


if (test == False) :
    scheduler = BlockingScheduler()

    # Schedules job_function to be run on the all minute
    scheduler.add_job(jobs, 'cron', minute=(1) )

    scheduler.start()
else :
    jobs()  