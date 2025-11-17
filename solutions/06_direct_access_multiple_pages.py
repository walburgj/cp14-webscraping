from helper_functions import clear_screen
clear_screen()

# ==========================
# CLICKING TO MULTIPLE PAGES
# ==========================

'''
OVERVIEW
--------
A big part of webscraping is navigating to multiple pages and grabbing data.

In this file, you'll do the same thing as the other file, but rather than
clicking on each link, you can just find the raw url data and then directly
visit each url by loading each one. If you can do it this way, this is more
efficient, but depending on how a website is set up, this may not always work
on some sites (mostly because some sites load the content in at the same url,
called a "single page application" rather than loading in a whole new page)
'''

# 1. GRAB DETAILS FROM EACH DETAIL PAGE WITHOUT USING .click():
# Set up playwright and go to the page below as a starting point for grabbing
# all the necessary data. You need to find the clickable link for each book
# on the page, but instead of clicking on it, find the url and use page.goto()
# to directly go to each individual site after you've found all the URLS.
# On each page, grab the title, price and description. Store the info for each
# book and output it to an excel file using pandas.

page_url = 'https://books.toscrape.com/catalogue/page-2.html'
base_url = 'https://books.toscrape.com/catalogue/'
from playwright.sync_api import sync_playwright
import pandas as pd

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=250)
    context = browser.new_context()
    page = context.new_page()

    page.goto(page_url)

    all_div_image_links = page.locator("div[class='image_container'] a")
    book_info_list = []
    url_list = []

    # grab all of the urls from each book image
    for index in range(all_div_image_links.count()):
        book_link = all_div_image_links.nth(index)
        # if you look inside the html, you'll notice the urls all use relative
        # links
        url = base_url + book_link.get_attribute('href')
        url_list.append(url)

    # now that we have all the urls, go through each and load each page directly
    for url in url_list:
        page.goto(url)
        title = page.locator('h1').first.text_content()
        price = page.locator("p[class='price_color']").first.text_content()
        description = page.locator("div[id='product_description'] + p").text_content()

        book_info_dict = {"title": title, "price": price, "description": description}
        book_info_list.append(book_info_dict)

df = pd.DataFrame(book_info_list)
df.to_excel("book_data.xlsx")
