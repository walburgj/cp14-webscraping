from helper_functions import clear_screen
clear_screen()

# =====================
# SCRAPING FUNDAMENTALS
# =====================

# PRACTICE
'''
Using playwright, navigate to the page shown in the page_url below and try
to do the following:

1. Print the price of the first book shown
2. Print the price of all the books on the page
3. Print out the url of every book on the page
4. Challenge:
    - Make an empty list
    - Get the Title, Price and URL from each book on the page and store each
      in a dictionary, like:
        book_info = {title: '', price: '', url: ''}
    - Append each book's dictionary into the empty list (so one dictionary for
      each book, the list has multiple dictionaries stored in it)
    - When you've gone through all books, convert your list into a Pandas
      DataFrame, then export it to an Excel file.
'''

page_url = 'https://books.toscrape.com/catalogue/page-2.html'

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=250)
    context = browser.new_context()
    page = context.new_page()

    page.goto(page_url)




    