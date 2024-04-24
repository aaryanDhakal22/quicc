from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import pytz
import time


class EmployeeClockTest(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self):
        try:
            punch_btn = self.browser.find_element(By.ID, "punch-btn")
            self.assertEqual(punch_btn.text, "Clock Out")
            punch_btn.click()
        except:
            print("No logout button")
        self.browser.quit()

    def check_for_row_in_table(self, table_name, row_text):
        log_table = self.browser.find_element(By.ID, table_name)
        rows = log_table.find_elements(By.TAG_NAME, "tr")
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_login(self):
        USER_NAME = "alisha"

        # Alisha opens the website ready to start the day
        self.browser.get("http://localhost:8000")

        # She puts in her username and password
        username_box = self.browser.find_element(By.ID, "username")
        username_box.send_keys(USER_NAME)
        password_box = self.browser.find_element(By.ID, "password")
        password_box.send_keys("admin")

        # Presses the login button to login to the website
        login_btn = self.browser.find_element(By.ID, "login-btn")
        login_btn.click()

        # She is successfully logged in
        login_badge_name = self.browser.find_element(By.ID, "login-name")
        self.assertEqual(login_badge_name.text, USER_NAME)

        # She sees that she is just an employee and needs to work harder to be the manager
        login_badge_type = self.browser.find_element(By.ID, "login-type")
        self.assertEqual(login_badge_type.text, "Employee")

        # She sees the time on the clock
        time.sleep(1)
        us_time_clock = self.browser.find_element(By.ID, "us-clock")
        self.assertEqual(us_time_clock.text, datetime.now().strftime("%I:%M %p"))
        ph_time_clock = self.browser.find_element(By.ID, "ph-clock")
        self.assertEqual(
            ph_time_clock.text,
            datetime.now(pytz.timezone("Asia/Manila")).strftime("%I:%M %p"),
        )

        # She sees the clock in button
        punch_btn = self.browser.find_element(By.ID, "punch-btn")
        self.assertEqual(punch_btn.text, "Clock In")

        # She clocks in
        clock_in_time = datetime.now().strftime("%I:%M:%S %p")
        punch_btn.click()

        # She watches the clock in button change to clock out button
        punch_btn = self.browser.find_element(By.ID, "punch-btn")
        self.assertEqual(punch_btn.text, "Clock Out")

        # She sees the time that she clocked in at
        self.check_for_row_in_table("clock-in-table", clock_in_time)

        # She then clocks out after a few hours
        time.sleep(4)
        clock_out_time = datetime.now().strftime("%I:%M:%S %p")
        punch_btn.click()
        logout_btn = self.browser.find_element(By.ID, "logout-btn")
        logout_btn.click()

        # At the end of the day she sees her logs for the day

        # She puts in her username and password
        username_box = self.browser.find_element(By.ID, "username")
        username_box.send_keys(USER_NAME)
        password_box = self.browser.find_element(By.ID, "password")
        password_box.send_keys("admin")

        # Presses the login button to login to the website
        login_btn = self.browser.find_element(By.ID, "login-btn")
        login_btn.click()
        self.check_for_row_in_table("clock-in-table", clock_in_time)
        self.check_for_row_in_table("clock-out-table", clock_out_time)

        # She logs out of the system
        logout_btn = self.browser.find_element(By.ID, "logout-btn")
        logout_btn.click()
        self.fail("Finish the test")

    # def test_can_see_prev_logs(self):
    # Alisha opens the website ready to start the day
    # She puts in her username and password and logs in to the system
    # She is successfully logged in
    # She notices the time and what time she is clocking in at and also her past clock in

    # She chooses what organization she is clocking in for and clocks in


if __name__ == "__main__":  #
    unittest.main()
