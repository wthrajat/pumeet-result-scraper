from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://results.puexam.in/HomePage.aspx")
driver.find_element(By.ID, "ctl00_LinkButton_Entrance").click()
driver.find_element(By.ID, "ctl00_LinkButton7").click()
driver.find_element(By.ID, "ctl00_cph1_lbtn_PUM").click()

for roll in range(900001, 900394):

    driver.find_element(By.ID, "ctl00_cph1_txtRollNo").clear()
    driver.find_element(By.ID, "ctl00_cph1_txtRollNo").send_keys(roll)
    driver.find_element(By.ID, "ctl00_cph1_btnShowResult").click()

    if "Absent" not in driver.page_source:
        name = driver.find_element(By.ID, "ctl00_cph1_lblCName").text
        marks = driver.find_element(By.ID, "ctl00_cph1_lblMarks").text
        rank = driver.find_element(By.ID, "ctl00_cph1_lblRank").text
        rollNo = driver.find_element(By.ID, "ctl00_cph1_lblRollNo").text

        print(rollNo + "," + name + "," + marks + "," + rank)
    else:
        print(f"{roll} was absent lmao 2200 Rs ka choona")

    driver.find_element(By.ID, "ctl00_cph1_btnBack").click()

print("\nJai Shri Parshuraam!")

driver.quit()
