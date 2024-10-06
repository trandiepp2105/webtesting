# UI TESTING USING SELENIUM WITH PYTHON

This repository contains the base setup of an UI testing project, using Python, Selenium Webdriver.

# 1. Instalation

## 1.1. Using Docker (Recommended)

Download or clone the repository

```
git clone https://github.com/trandiepp2105/webtesting.git
cd webtesting

```

Run docker compose
From the project root directory run:

```
docker-compose up --build -d
```

## 1.2. Using in virtualenv or local (Not Recommended)

Download source code and install environment:

```
git clone https://github.com/trandiepp2105/webtesting.git
cd webtesting
pip install -r requirements.txt
```

# 2. Run test cases

## 2.1. Run in docker container.

```
docker exec webtesting "python ./main.py --test-case={test-case}"
```

## 2.2. Run in local or virtualenv

```
python ./main.py --test-case={test-case}
```

Command line parameter explanation:

- --test-case: name of the test case you want to run

List test case:

- signup: Simulate user account registration steps
- login: Simulate user login steps
- product: Simulate user product browsing process
