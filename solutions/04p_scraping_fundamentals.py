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

# 1. Price of the first book

    print(page.locator('p[class="price_color"]').nth(0).text_content())

# 2. Price of all books on the page
    all_price_p = page.locator('p[class="price_color"]')

    for index in range(all_price_p.count()):
        print(index, all_price_p.nth(index).text_content())

# 3. URL of every book
# Note there's lots of ways you could have done this. The URL of each book
# is stored in multiple locations
    all_article_product_pods = page.locator("article[class='product_pod']")

    for index in range(all_article_product_pods.count()):
        book_url = all_article_product_pods.nth(index).locator('a').nth(0).get_attribute('href')
        print(index, book_url)  

# 4. Storing data and exporting it
    book_info_list = []
    all_article_product_pods = page.locator("article[class='product_pod']")
    for index in range(all_article_product_pods.count()):
        specific_product_pod = all_article_product_pods.nth(index)
        title = specific_product_pod.locator('h3').first.text_content()
        price = specific_product_pod.locator('p[class="price_color"]').first.text_content()
        url = specific_product_pod.locator('a').first.get_attribute('href')
        url = "https://books.toscrape.com/catalogue/" + url
        book_dict = {'title': title, 'price': price, 'url': url}
        book_info_list.append(book_dict)

    import pandas as pd

    df = pd.DataFrame(book_info_list)
    df.to_excel("book_data.xlsx", index=False)

    