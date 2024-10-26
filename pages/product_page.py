from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import time
import math

def is_element_in_viewport(driver, element):
    return driver.execute_script("""
        var rect = arguments[0].getBoundingClientRect();
        var windowHeight = (window.innerHeight || document.documentElement.clientHeight);
        var windowWidth = (window.innerWidth || document.documentElement.clientWidth);
        
        // Kiểm tra nếu phần tử có bất kỳ phần nào nằm trong viewport
        var vertInView = (rect.top <= windowHeight) && ((rect.top + rect.height) >= 0);
        var horInView = (rect.left <= windowWidth) && ((rect.left + rect.width) >= 0);

        return vertInView && horInView;
    """, element)

class ProductPage(BasePage):

    def open(self, homepage_url, collection_name = "Baby Tee & Váy", scroll_quantity = 3):
        """
        Open the home page and follow the steps to open the login page.
        
        Args:
            homepage_url (str): Home page URL
            collection_name (str): Name of the collection to open. Default is "Baby Tee & Váy"
            scroll_quantity (int): Number of times to scroll down the page. Default is 3
        """
        # Mở trang chính
        super().open(homepage_url)
        
        try:
            
            self.hover_and_click(By.CSS_SELECTOR, f'a[title="{collection_name}"]')

            time.sleep(5)
            window_size = self.driver.get_window_size()

            browser_height_center = math.ceil(window_size['height'] / 2)
            
            for _ in range(scroll_quantity):
                self.scroll_vertical_by_amount(browser_height_center)
                time.sleep(1)
            self.scroll_vertical_by_amount(180)
            time.sleep(1)


            product_blocks = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_all_elements_located((By.CLASS_NAME, "product-block"))
            )
            visible_products = []
            for product in product_blocks:
                if is_element_in_viewport(self.driver, product):
                    element = product.find_element(By.TAG_NAME, 'a')
                    product_title = element.get_attribute("title")
                    visible_products.append(element)
                    print(f"Product is displayed: {product_title}")
            if visible_products:
                self.visible_products = visible_products
        except TimeoutException:
            print("Login button not found or page did not load in time.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def goto_detail_product(self):
        """
        Navigates to the detail page of the last visible product on the current page.

        This method checks if there are any visible products. If so, it moves the mouse to 
        the last visible product with a slight offset (50, 50), waits for 2 seconds, and 
        clicks on it to navigate to its detail page. After the click, the method waits for 
        the detail page to fully load.

        Raises:
            Exception: If the page fails to load or no products are visible.

        Steps:
            1. Check if the list of visible products is not empty.
            2. Select the last visible product from the list.
            3. Use ActionChains to move to the last product with a (50, 50) pixel offset.
            4. Wait for 2 seconds before performing the click.
            5. Click on the last product and wait for the page to fully load.
        """
        if self.visible_products:
            last_product = self.visible_products[-1]

            # Scroll the product into the center of the viewport
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", last_product)

            # Optional: Adjust further if needed
            time.sleep(1)
            actions = ActionChains(self.driver)
            actions.move_to_element_with_offset(last_product, 50, 50).perform()
            time.sleep(2)
            actions.click().perform()
            self.wait_for_page_load()
    
    def simulate_add_to_cart_action(self, scroll_down_quantity = 11, scroll_up_quantity = 8):
        """
        Simulates the 'Add to Cart' action by scrolling down and up the page and 
        then hovering over and clicking the 'Add to Cart' button.

        Args:
            scroll_down_quantity (int): Number of scrolls down the page. Default is 11.
            scroll_up_quantity (int): Number of scrolls up the page. Default is 8.

        Behavior:
            - Scrolls down the page by a fixed amount (200 pixels) multiple times.
            - Scrolls up by the same amount for a specified number of times.
            - If scrolling down reaches the bottom or scrolling up reaches the top, 
            the loop breaks early.
            - Finally, it performs a hover and click action on the 'Add to Cart' button.
        """
        for _ in range(scroll_down_quantity):
            if not self.can_scroll_down():  # Check if we can still scroll down
                print("Cannot scroll down!")
                break
            self.scroll_vertical_by_amount(200)
            time.sleep(0.2)
        for _ in range(scroll_up_quantity):
            if not self.can_scroll_up():  # Check if we can still scroll up
                break
            self.scroll_vertical_by_amount(-200)
            time.sleep(0.2)         
        
        self.scroll_vertical_by_amount(-100)

        self.hover_and_click(By.CSS_SELECTOR, 'button#add-to-cart', delay=2)

    def close_gift_popup(self):
        """
        Closes the gift popup if it appears on the page.

        This method waits for the 'product-gift-wrap' element to become visible, indicating
        that the gift popup has appeared. Once the popup is detected, it hovers over and 
        clicks the 'btn-buygift' button to close the popup.

        If the popup does not appear within 10 seconds or another error occurs during the 
        process, an exception is caught, and an error message is printed.

        Raises:
            TimeoutException: If the 'product-gift-wrap' element does not appear within 10 seconds.
            Exception: If any error occurs during the hover and click action.

        Behavior:
            1. Wait for the 'product-gift-wrap' element to appear (up to 10 seconds).
            2. Hover over and click the 'btn-buygift' button to close the popup.
            3. Print a success message if the popup is closed successfully.
            4. If an exception occurs, print the failure message with details.
        """
        try:
            # waiting for the product-gift button appear
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "product-gift-wrap"))
            )

            self.hover_and_click(By.CLASS_NAME, "btn-buygift")
            print("PRESS OK TO CLOSE GIFT POPUP!.")
            
        except Exception as e:
            print(f"FAILED: {e}")

    def click_view_cart_button(self):
        """
        Clicks the 'View Cart' button on the page.

        This method hovers over and clicks the 'View Cart' button, identified by the 
        CSS selector 'a.linktocart.button.dark'. A slight delay is added before the 
        click action to ensure the button is fully interactive. If the action is successful, 
        a success message is printed. In case of failure, an exception is caught, and an error 
        message is printed with the exception details.

        Args:
            None

        Raises:
            Exception: If there is an issue during the hover and click action.

        Behavior:
            1. Hover over and click the 'View Cart' button.
            2. Print a success message after the button is clicked.
            3. If an exception occurs, print an error message with the exception details.
        """
        try:
            self.hover_and_click(By.CSS_SELECTOR, "a.linktocart.button.dark", delay=2)
            print("PRESS CART BUTTON!")
            
        except Exception as e:
            print(f"FAILED WHILE FINDING THE CART BUTTON: {e}")