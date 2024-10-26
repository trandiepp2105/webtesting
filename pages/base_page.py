from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
import time
import threading
import math

test_var = 1

class BasePage:
    def __init__(self, driver):
        """
        Initializes the BasePage with the specified WebDriver.

        Args:
            driver (WebDriver): The Selenium WebDriver instance used to control the browser.
        """
        self.driver = driver

    def wait_for_page_load(self, timeout=10):
        """
        Waits for the logo image with specific attributes to load and be fully visible.

        Args:
            timeout (int): Maximum time to wait for the image to load. Default is 10 seconds.
        """
        try:
            self.wait_for_element(By.CSS_SELECTOR, 'a[title="Đăng nhập"]', timeout)
            print("LOAD PAGE SUCCESSFULLY!")
        except TimeoutException:
            print("LOAD PAGE FAILED!")

    def open(self, url):
        """
        Opens the specified URL in the browser and waits for the page to load.

        Args:
            url (str): The URL of the webpage to open.
        """
        self.driver.get(url)
        print("GET PAGE SUCCESSFULLY!")
        self.wait_for_page_load()

    def go_back_home(self):
        """
        Navigate back to the home page by clicking on the logo element.

        This method waits for the logo element, located by the CSS selector 'div.wrap-logo a[href="https://tsunsg.com"]', 
        to become visible on the page and then clicks it to redirect the user to the home page.

        Raises:
            TimeoutException: If the logo element does not appear within the specified wait time.
        """
        logo = self.wait_for_element(By.CSS_SELECTOR, 'div.wrap-logo a[href="https://tsunsg.com"]')
        logo.click()

    def close(self):
        """
        Closes the browser and ends the WebDriver session.
        """
        self.driver.quit()

    def wait_for_element(self, by, value, timeout=5):
        """
        Waits for an element to become visible on the page.

        Args:
            by (By): The method used to locate the element (e.g., By.ID, By.NAME).
            value (str): The locator value for the element.
            timeout (int): Maximum time to wait for the element to appear. Default is 10 seconds.

        Returns:
            WebElement: The WebElement if found, raises an exception otherwise.
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(
                # EC.visibility_of_element_located((by, value))
                EC.element_to_be_clickable((by, value))
            )
            return element
        except TimeoutException as e:
            print(f"Could not find element with {by} = {value}: {e}")
            raise

    def scroll_vertical_by_amount(self, y, steps=10, delay=0.05):
        """
        Scroll vertically on the page by a specified amount.

        This method scrolls the page vertically by the given `y` distance, divided into multiple steps. 
        The scrolling is performed in `steps` number of increments, with an optional delay between each scroll step.

        Args:
            y (int): The total vertical distance to scroll in pixels.
            steps (int, optional): The number of scroll steps. Default is 10.
            delay (float, optional): The delay (in seconds) between each scroll step. Default is 0.05 seconds.

        Raises:
            TimeoutException: If an issue occurs during scrolling.

        """
        actions = ActionChains(self.driver)

        # Calculate the distance for each scroll step
        step_distance = math.ceil(y / steps)
        
        for _ in range(steps):
            actions.scroll_by_amount(0, step_distance).perform()  # Scroll vertically by step distance
            time.sleep(delay)  # Wait for the specified delay between each scroll

    def fill_input_field(self, by, value, input_text):
        """
        Fills in an input field specified by the locator.

        Args:
            by (By): The method used to locate the input field (e.g., By.ID, By.NAME).
            value (str): The locator value for the input field.
            input_text (str): The text to input into the field.

        Raises:
            Exception: If the field is not found or cannot be filled.
        """
        try:
            input_field = self.wait_for_element(by, value, 2)  # Wait for the field to be present
            # simulate input delay
            for char in input_text:
                input_field.send_keys(char)  # Send each character one by one
                time.sleep(0.2)
        except Exception as e:
            raise Exception(f"Could not fill the input field: {e}")

    def hover_and_click(self, by, value, delay=1):
        """
        Hovers over an element and clicks it.

        Args:
            by (str): The method to locate the element (e.g., By.CSS_SELECTOR).
            value (str): The value to locate the element.
            delay (int): Optional delay before clicking.
        """
        try:
            # Find the element and hover over it
            element = self.wait_for_element(by, value)

            if(element):
                # Create an action chain to perform the hover action
                actions = ActionChains(self.driver)
                actions.move_to_element(element).perform()
                # Wait for the specified delay before clicking
                time.sleep(delay)
                # Click the element
                element.click()
            
        
        except Exception as e:
            print(f"Error while hovering and clicking: {e}")
    
    def hover_element(self, by, value, delay = 2):
        element = self.wait_for_element(by, value)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        time.sleep(delay)

    def get_element_text(self, by, value):
        """
        Gets the text content of an element.

        Args:
            by (By): The method used to locate the element (e.g., By.ID, By.CSS_SELECTOR).
            value (str): The locator value for the element.

        Returns:
            str: The text content of the element.
        """
        try:
            element = self.wait_for_element(by, value)
            return element.text
        except Exception as e:
            raise Exception(f"Could not get text from the element: {e}")

    def can_scroll_down(self):
        """Check if the page can scroll down further."""
        return self.driver.execute_script('return (window.innerHeight + window.scrollY) < document.body.scrollHeight')
        
    def can_scroll_up(self):
        """Check if the page can scroll up further."""
        return self.driver.execute_script('return window.scrollY > 0')