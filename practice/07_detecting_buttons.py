from helper_functions import clear_screen
clear_screen()

# =================
# DETECTING BUTTONS
# =================

'''
OVERVIEW
--------
Many times when navigating webpages, you'll want to detect whether a specific
element exists (like a "next page" button) before trying to click on it.

KEY METHODS
-----------

.count() == 0
    - after using .locator for any element, you'll want to use .count() == 0
      to check if that element exists. Only interact with it if it exists,
      otherwise you'll get an error.

'''

# 1. GRAB DETAILS FROM EACH DETAIL PAGE:
# You are given starting code that already visits the book data of each page.
# Now, make it find the "next" button at the bottom right of each page. Continue
# scraping all the book data from each page until there are no longer any pages
# to go to.

page_url = 'https://books.toscrape.com/catalogue/page-47.html'

from playwright.sync_api import sync_playwright
import pandas as pd

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=0)
    context = browser.new_context()
    page = context.new_page()

    page.goto(page_url)
    book_info_list = []

    print(f"Current URL: {page.url}")
    all_div_image_containers = page.locator("div[class='image_container']")

    for index in range(all_div_image_containers.count()):
        book_div = all_div_image_containers.nth(index)
        # go to the page of the specific book
        book_div.click()
        # just for safety, wait until the data you want on the page has loaded
        # for a site like this, this probably isn't necessary, but on other
        # more interactive websites, this can really help
        page.wait_for_selector('h1')
        print(f"Current detail page url: {page.url}")
        title = page.locator('h1').first.text_content()
        price = page.locator("p[class='price_color']").first.text_content()
        description_element = page.locator("div[id='product_description'] + p")
        if description_element.count() > 0:
            description = description_element.text_content()
        else:
            description = None

        book_info_dict = {"title": title, "price": price, "description": description}
        book_info_list.append(book_info_dict)

        page.go_back()
        page.wait_for_selector("div[class='image_container']")
        # select it again since we changed pages
        all_div_image_containers = page.locator("div[class='image_container']")


df = pd.DataFrame(book_info_list)
df.to_excel("book_data.xlsx")


'''
EXTRA TIP
---------
Using .count() == 0 is generally good practice. However, in some situations,
website will keep the element on the page, but deactivate it or make it
invisible in some way. In instances like that, .count() would return 1 instead
of 0. So, you should use . is_visible() instead. That will return True or False
depending on if the element that exists is visible/interactible.
'''