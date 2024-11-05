from pages.login_page import LoginPage
import traceback
import time
from selenium import webdriver
from selenium.webdriver.edge.options import Options

user_profiles_data = [
[
("last_name", "Ngô Thị"),           
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
("password", "Chamanh0506"),
],
[
("last_name", "Ngô Thị"),           
("first_name", "Châm Anh"),
("gender", "Nữ"),
("birthday", "06/05/2003"),
("email", "chamanh050603@gmail.com"),     
("password", "Chamanh0506@"),
],
[
("last_name", "Ngô Thị"),           
("first_name", "Châm Anh"),
("gender", "Nữ"),
("birthday", "06/05/2003"),
("email", ""),     
("password", "Chamanh0506@"),
],
[
("last_name", "Ngô Thị"),           
("first_name", "Châm Anh"),
("gender", "Nữ"),
("birthday", "06/05/2003"),
("email", "chamanh0506@gmail.com"),     
("password", ""),
],
[
("last_name", "Ngô Thị"),           
("first_name", "Châm Anh"),
("gender", "Nữ"),
("birthday", "06/05/2003"),
("email", "chamanh0506gmail.com"),     
("password", "Chamanh0506@"),
],
]

edge_options = Options()
edge_options.use_chromium = True
edge_options.add_argument("--start-maximized")  
edge_options.add_argument("--no-sandbox")  
edge_options.add_argument("--disable-dev-shm-usage")

def login(homepage_url, user_profiles = user_profiles_data):
    
    for user_profile in user_profiles:
        driver = webdriver.Edge(options=edge_options) 
        login_page = LoginPage(driver)
        try:
            login_page.open(homepage_url)
            login_page.fill_login_form(user_profile)
        except Exception as e:
            print(f"Có lỗi xảy ra: {e}")
            print(traceback.format_exc())  
        
        finally:
            time.sleep(3)
            login_page.close()  