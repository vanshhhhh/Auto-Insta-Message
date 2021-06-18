from selenium import webdriver
from time import sleep
import pyautogui

def check():
    c=0
    #login
    username=input("Enter your username : ")
    pw=input("Enter your password : ")
    #options = webdriver.ChromeOptions()
    #options.add_argument('headless')
    driver = webdriver.Chrome()
    driver.get("https://instagram.com")
    sleep(2)
    
    driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")\
        .send_keys(username)
    driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")\
        .send_keys(pw)
    driver.find_element_by_xpath('//button[@type="submit"]')\
        .click()
    sleep(4)
    driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
        .click()
    sleep(2)
    driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
        .click()
    #message checking start
    sleep(1)
    driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a")\
        .click()
    sleep(4)
    
    try:
        while True:
            driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[1]/a/div/div[3]/div')\
                .click()
            driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")\
                .send_keys("This is an automated reply by the bot. User is not available currently")
            sleep(1)
            driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button")\
                .click()
            c+=1
    except Exception:
        if c>0:
            print("Auto-reply sent to unread messages")
            pyautogui.alert("Auto-reply sent to unread messages")
        else:
            print("No new messages")
            pyautogui.alert("\nNo new messages")
    pyautogui.alert("\n\nProgram completed \nBot exiting...")
    sleep(3)
check()

