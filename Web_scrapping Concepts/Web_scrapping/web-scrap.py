from bs4 import BeautifulSoup
import urllib
import re
import time
import pandas as pd
import os
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


home_page = "https://prs.moh.gov.sg/prs/internet/profSearch/main.action?hpe=SPC"

# Use urllib to open home page, and BeautifulSoup to parse HTML
home_page_content = urllib.request.urlopen(home_page)
home_page_html = BeautifulSoup(home_page_content, 'html.parser')
print(home_page_html,'@@@@@')
# Note: Please see Jupyter Notebook to see the HTML returned