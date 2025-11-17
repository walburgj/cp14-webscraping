from helper_functions import clear_screen
clear_screen()

# ==========================
# CLICKING TO MULTIPLE PAGES
# ==========================

'''
OVERVIEW
--------
A big part of webscraping is navigating to multiple pages and grabbing data.
Because playwright is controlling a browser, you can use python to tell it to 
click where you want to control the browser as if a human were using it.

KEY METHODS
-----------

.click()
    - Use after you've found a specific element that you want to click on. This
      is the same as your mouse clicking on that part of the webpage.

page.wait_for_selector('element_name')
    - This will pause your python code until playwright makes sure that the
      specific element you are looking for has loaded. Not really necessary
      for the type of scraping we're doing, but good to be aware of.

page.go_back()
    - Exactly like clicking the back button in your browser. Will go to the
      previous page.

'''

# 1. GRAB DETAILS FROM EACH DETAIL PAGE:
# Set up playwright and go to the page below as a starting point for grabbing
# all the necessary data. You need to find the clickable link for each book
# on the page, then click on it using .click() and grab the title, price and
# description. Store the info for each book and output it to an excel file
# using pandas.

page_url = 'https://books.toscrape.com/catalogue/page-2.html'

import pandas as pd
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=250)
    context = browser.new_context()
    page = context.new_page()

    page.goto(page_url)

