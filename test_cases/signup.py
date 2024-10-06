from pages.signup_page import SignupPage
import traceback
import time
user_profile_data = [
    ("last_name", "Trần Văn"),           
    ("first_name", "Điệp"),
    ("gender", "Nam"),
    ("birthday", "05/21/2003"),
    ("email", "tranvandiepp2105@gmail.com"),     
    ("password", "Diep2105@"),
]

def signup(driver, homepage_url, user_profile = user_profile_data):
    signup_page = SignupPage(driver)
    try:
        signup_page.open(homepage_url)
        signup_page.fill_registration_form(user_profile)
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")
        print(traceback.format_exc())  
    
    finally:
        time.sleep(5)
        signup_page.close()  