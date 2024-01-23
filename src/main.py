from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.get("https://results.puexam.in/HomePage.aspx")
driver.find_element(By.ID, "ctl00_LinkButton_Entrance").click()
driver.find_element(By.ID, "ctl00_LinkButton7").click()
driver.find_element(By.ID, "ctl00_cph1_lbtn_PUM").click()

print("{:<10} {:<30} {:<10} {:<10}".format("RollNo", "Name", "Marks", "Rank"))
print("="*70)
for roll in range(900001, 900394):

    driver.find_element(By.ID, "ctl00_cph1_txtRollNo").clear()
    driver.find_element(By.ID, "ctl00_cph1_txtRollNo").send_keys(roll)
    driver.find_element(By.ID, "ctl00_cph1_btnShowResult").click()
    name = driver.find_element(By.ID, "ctl00_cph1_lblCName").text
    rollNo = driver.find_element(By.ID, "ctl00_cph1_lblRollNo").text

    if (("Not Qualified" not in driver.page_source) and ("Absent" not in driver.page_source)):
        marks = driver.find_element(By.ID, "ctl00_cph1_lblMarks").text
        rank = driver.find_element(By.ID, "ctl00_cph1_lblRank").text
        line = "{:<10} {:<30} {:<10} {:<10}".format(rollNo, name, marks, rank)
        print(line)
    else:
        print(f"{roll} {name} was absent.") if ("Absent" in driver.page_source) else print(f"{roll} {name} did not qualify.")
    driver.find_element(By.ID, "ctl00_cph1_btnBack").click()

print("="*70)

driver.quit()
