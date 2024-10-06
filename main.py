import os
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from dotenv import load_dotenv
from test_cases.signup import signup
from test_cases.login import login
from test_cases.product import product
import argparse
from enum import Enum
load_dotenv()  


class TestCase(Enum):
    SIGNUP = "signup"
    LOGIN = "login"
    PROFILE_UPDATE = "browse-products"
def main():

    edge_options = Options()
    edge_options.add_argument("--start-maximized")  
    edge_options.add_argument("--no-sandbox")  
    edge_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Edge(options=edge_options)  

    homepage_url = os.getenv('WEBSITE_LINK') 

    # Initialize the parameter analyzer
    parser = argparse.ArgumentParser(description="Run test cases")
    # Add --test-case parameter
    parser.add_argument('--test-case', type=str, help="Name of test case to run")

    # Parsing parameters from command line
    args = parser.parse_args()

    # Get the value of --test-case and process it

 
    if args.test_case:
        print(f"Start running test case: {args.test_case}")
        if args.test_case == TestCase.SIGNUP.value:
            signup(driver, homepage_url)
        elif args.test_case == TestCase.LOGIN.value:
            login(driver, homepage_url)
        elif args.test_case == TestCase.PROFILE_UPDATE.value:
            product(driver, homepage_url)
    else:
        print("No test cases are passed in!")

if __name__ == "__main__":
    main()
