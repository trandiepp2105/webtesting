from pages.signup_page import SignupPage
import traceback
import time
user_profiles_data = [[
("last_name", "Ngô Thị"),           
("first_name", "Châm Anh"),
("gender", "Nữ"),
("birthday", "06/05/2003"),
("email", "chamanh0506@gmail.com"),     
("password", "Chamanh0506@"),
], [
("last_name", "Ngô Thị"),           
("first_name", "Châm Anh"),
("gender", "Nữ"),
("birthday", "06/05/2003"),
("email", "chamanh0506@gmail.com"),     
("password", "Chamanh0506@"),
], [
("last_name", "x"),           
("first_name", "x"),
("gender", "Nữ"),
("birthday", "x"),
("email", "chamanh0506@gmail.com"),     
("password", "x"),
], [
("last_name", "Ngô Thị"),           
("first_name", "Châm Anh"),
("gender", "Nữ"),
("birthday", "06/05/2003"),
("email", "chamanh0506gmail.com"),     
("password", "Chamanh0506@"),
], [
("last_name", "Ngô Thị"),           
("first_name", "Châm Anh"),
("gender", "Nữ"),
("birthday", "06/05/2003"),
("email", "chamanh0506@gmail"),     
("password", "Chamanh0506@"),
], 
[
("last_name", "Ngô Thị"),           
("first_name", "Châm Anh"),
("gender", "Nữ"),
("birthday", ""),
("email", "chamanh0506@gmail.com"),     
("password", "Chamanh0506@"),
],
[
("last_name", "Ngô Thị"),           
("first_name", "Châm Anh"),
("gender", ""),
("birthday", "06/05/2003"),
("email", "chamanh0506@gmail.com"),     
("password", "Chamanh0506@"),
],
[
("last_name", ""),           
("first_name", "Châm Anh"),
("gender", "Nữ"),
("birthday", "06/05/2003"),
("email", "chamanh0506@gmail.com"),     
("password", "Chamanh0506@"),
],
[
("last_name", "Ngô Thị"),           
("first_name", "Châm Anh"),
("gender", "Nữ"),
("birthday", "06/05/2003"),
("email", "chamanh0506@gmail.com"),     
("password", "Cham"),
]
]

def signup(driver, homepage_url, user_profiles = user_profiles_data):

    signup_page = SignupPage(driver)
    for  user_profile in user_profiles:
        try:
            signup_page.open(homepage_url)
            signup_page.fill_registration_form(user_profile)
        except Exception as e:
            print(f"Có lỗi xảy ra: {e}")
            print(traceback.format_exc())  
        
        finally:
            time.sleep(3)
    signup_page.close()      