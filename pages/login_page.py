from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import selenium
from pages.base_page import BasePage
import time
class LoginPage(BasePage):
    def open(self, homepage_url):
        """
        Open the home page and follow the steps to open the login page.
        
        Args:
            homepage_url (str): Home page URL
        """
        # Mở trang chính
        super().open(homepage_url)
        
        try:
            
            self.hover_and_click(By.CSS_SELECTOR, 'span.icon-account a[title="Đăng nhập"]')

            
            WebDriverWait(self.driver, 5).until(
                EC.url_contains("/account/login")  
            )
            
            self.wait_for_page_load()
            self.scroll_vertical_by_amount(130)
        except TimeoutException:
            print("Login button not found or page did not load in time.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def fill_login_form(self, user_profile):
            """
            Fills the registration form with user information.
            """
            try:
                for id, value in user_profile:
                    if id == "email":
                        self.scroll_to_and_fill("customer_email", value)
                    if id == "password":
                        self.scroll_to_and_fill("customer_password", value)
                time.sleep(1)
                # Nhấn vào nút đăng ký
                self.hover_and_click(By.CSS_SELECTOR, 'input.btn[type="submit"][value="Đăng nhập"]')
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
            else:
                # If input field not gender then field string into input field.
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

