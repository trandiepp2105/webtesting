from pages.login_page import LoginPage
import traceback
import time
user_profile_data = [
    ("last_name", "Trần Văn"),           
    ("first_name", "Điệp"),
    ("radio2", ""),
    ("birthday", "05/21/2003"),
    ("email", "tranvandiepp2105@gmail.com"),     
    ("password", "Diep2105@"),
]

def login(driver, homepage_url, user_profile = user_profile_data):
    login_page = LoginPage(driver)
    try:
        login_page.open(homepage_url)
        login_page.fill_login_form(user_profile)
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")
        print(traceback.format_exc())  
    
    finally:
        time.sleep(5)
        login_page.close()  