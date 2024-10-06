from selenium import webdriver
import os


from dotenv import load_dotenv

# Tải các biến môi trường từ file .env
load_dotenv()

# Initialize Edge WebDriver
driver = webdriver.Edge()  


# Get the link of the website to be tested
WEBSITE_LINK = os.getenv('WEBSITE_LINK')

# open website with edge browser 
driver.get(WEBSITE_LINK)

input("Nhấn Enter để đóng trình duyệt...")

driver.close() 
