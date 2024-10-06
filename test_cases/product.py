from pages.product_page import ProductPage
import traceback
import time

list_collections_name = [
    "Mới Nhất",
    "Bán Chạy",
    "Áo Thun",
    "Baby Tee & Váy",
    "Áo Khoác",
]


def product(driver, homepage_url):
    product_page = ProductPage(driver)
    try:
        product_page.open(homepage_url, list_collections_name[0])
        product_page.goto_detail_product()
        product_page.simulate_add_to_cart_action(scroll_down_quantity=10, scroll_up_quantity=7)
        product_page.close_gift_popup()
        time.sleep(1.5)
        product_page.click_view_cart_button()
        product_page.go_back_home()
    except Exception as e:
        print(f"An error occurred while browsing the product: {e}")
        print(traceback.format_exc())  
    
    finally:
        time.sleep(5)
        product_page.close() 
    
