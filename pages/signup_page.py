from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import selenium
from pages.base_page import BasePage
import time
class SignupPage(BasePage):
    def open(self, homepage_url):
        """
        Open the home page and follow the steps to open the login page.
        
        Args:
            homepage_url (str): Home page URL
        """
        # Open the homepage
        super().open(homepage_url)
        
        try:
            # hover the element then click it
            self.hover_and_click(By.CSS_SELECTOR, 'span.icon-account a[title="Đăng nhập"]')

            # Checking the url whether the url contains "/account/login"
            WebDriverWait(self.driver, 5).until(
                EC.url_contains("/account/login")  
            )
            # waiting for the page to finish loading
            self.wait_for_page_load()
            # scroll 150px to find the register button
            self.scroll_vertical_by_amount(150)
            # Using hover_and_click function in order to move the mouse to "Đăng ký" button
            self.hover_and_click(By.CSS_SELECTOR, 'div.req_pass a[title="Đăng ký"]')

            self.wait_for_page_load()
            # self.scroll_vertical_by_amount(100)
        except TimeoutException:
            print("Login button not found or page did not load in time.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def fill_registration_form(self, user_profile):
        """
        Fills the registration form with user information.
        """
        try:
            for id, value in user_profile:
                if id == "gender":
                    if value == "Nam":
                        self.scroll_to_and_fill("radio2", value)
                    else:
                        self.scroll_to_and_fill("radio1", value)
                else:
                    self.scroll_to_and_fill(id, value)
            time.sleep(1)
            
            self.hover_and_click(By.CSS_SELECTOR, 'input.btn[type="submit"][value="Đăng ký"]')
            print("Registration button clicked.")

        except Exception as e:
            print(f"Error filling registration form: {e}")

    def scroll_to_and_fill(self, id, value):
        """
        Scrolls to the input field with the specified id and fills it with the provided value.
        
        Args:
            id (str): The id of the input field.
            value (str): The value to fill into the input field.
        """
        try:
            input_field = self.driver.find_element(By.CSS_SELECTOR, f"input#{id}")
            
            time.sleep(0.5)  

            if id == "radio2":
                # choose gender
                input_field.click()
            elif id == "radio1":
                # choose gender
                input_field.click()
            else:
                # Enter into another input field
                input_field.click()
                time.sleep(1)
                input_field.clear()  
                for char in value:
                    input_field.send_keys(char)  # Send each character one by one
                    time.sleep(0.1)
            # self.scroll_vertical_by_amount(50)
            print(f"Filled input '{id}' with value: {value}")

        except TimeoutException:
            print(f"Input field with id '{id}' not found.")
        except Exception as e:
            print(f"Error while filling input field with id '{id}': {e}")

