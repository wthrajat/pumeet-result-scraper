from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import os

driver = webdriver.Firefox()
driver.get("https://results.puexam.in/HomePage.aspx")
driver.find_element(By.ID, "ctl00_LinkButton_Entrance").click()
driver.find_element(By.ID, "ctl00_cph1_lbtn_PUM").click()

for roll in range(1000001, 1000394):
    if roll == 900040 or roll == 900390 or roll == 900346 or roll == 900336 or roll == 900333 or roll == 900307 or roll == 900306 or roll == 900300 or roll == 900279 or roll == 900049 or roll == 900053 or roll == 900061 or roll == 900088 or roll == 900095 or roll == 900114 or roll == 900122 or roll == 900152 or roll == 900158 or roll == 900162 or roll == 900171 or roll == 900174 or roll == 900192 or roll == 900207 or roll == 900277 or roll == 900268:
        continue
    driver.find_element(By.ID, "ctl00_cph1_txtRollNo").send_keys(roll)
    driver.find_element(By.ID, "ctl00_cph1_btnShowResult").click()
    # isPresent = driver.find_element(By.ID, "ctl00_cph1_lblResult")
    # print(isPresent.is_displayed())
    # if driver.find_element(By.ID, "ctl00_cph1_lblResult").is_displayed() is False:
    # ifGaandPhulanaIsAnArt.thenYouAreMasterOfIt(True)

    #Attributes
    name = driver.find_element(By.ID, "ctl00_cph1_lblCName").text

    marks = driver.find_element(By.ID, "ctl00_cph1_lblMarks").text
    rank = driver.find_element(By.ID, "ctl00_cph1_lblRank").text
    rollNo = driver.find_element(By.ID, "ctl00_cph1_lblRollNo").text

    #You may add sleep timer if u stalking by the "eyes"
    # time.sleep(x) x==in seconds
    line = rollNo + "," + name + "," + marks + "," + rank
    print(line)
    driver.find_element(By.ID, "ctl00_cph1_btnBack").click()
    roll += 1

print("\nJai Shri Parshuraam!")
