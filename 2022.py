from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
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

    if "Absent" not in driver.page_source or "Not Qualified" not in driver.page_source:
        name = driver.find_element(By.ID, "ctl00_cph1_lblCName").text
        marks = driver.find_element(By.ID, "ctl00_cph1_lblMarks").text
        rank = driver.find_element(By.ID, "ctl00_cph1_lblRank").text
        rollNo = driver.find_element(By.ID, "ctl00_cph1_lblRollNo").text

        line = "{:<10} {:<30} {:<10} {:<10}".format(rollNo, name, marks, rank)
        print(line)
    else:
        print(f"{roll} was absent, lmao 2200/- ka choona lag gaya!")
    driver.find_element(By.ID, "ctl00_cph1_btnBack").click()

print("="*70)
print("\nJai Shri Parshuraam!")

driver.quit()
