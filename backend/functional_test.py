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
        self.browser.quit()

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
        punch_btn.click()
        # She watches the clock in button change to clock out button
        self.assertEqual(punch_btn.text, "Clock Out")

        # Maybe add feature to disable button for accidental double press

        # She is greeted with a message
        self.assertEqual(self.browser.find_element(By.ID, "welcome-msg"), "Welcome!")

        self.fail("Finish the test")

    # def test_can_see_prev_logs(self):
    # Alisha opens the website ready to start the day
    # She puts in her username and password and logs in to the system
    # She is successfully logged in
    # She notices the time and what time she is clocking in at and also her past clock in

    # She chooses what organization she is clocking in for and clocks in


if __name__ == "__main__":  #
    unittest.main()
