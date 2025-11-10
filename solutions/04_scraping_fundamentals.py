from helper_functions import clear_screen
clear_screen()

# =====================
# SCRAPING FUNDAMENTALS
# =====================

'''
OVERVIEW
--------
Scraping successfully requires that you tell playwright where the data you want
exists. We're gonna do that with these methods below. There are other methods
and alternative ways to do things, but to keep it simple we'll focus on these.
    - .locator("element_name[attribute='attribute_value']")
        - will grab every element that matches
    
    - .first, .last, or .nth()
        - use in conjunction with .locator() to grab a specifc element if .locator
          is able to find multiple

    - .text_content() or .inner_text()
        - use in conjunction with .locator() to get the content of an element
        - .text_content() will preserve the original html formatting of some
          text, while inner_text() will grab just the text in a more normal
          formatting. Usually doesn't matter which you use.

    - .get_attribute('attribute_name')
        - use in conjunction with .locator() to get the value of a specific
          attribute in an element
'''

# 1. GO TO A PAGE USING PLAYWRIGHT:
# Set up playwright and go to the page below as a starting point for grabbing
# all the necessary data
page_url = 'https://books.toscrape.com/catalogue/aladdin-and-his-wonderful-lamp_973/index.html'

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    page.goto(page_url)


# 2. GET CONTENT FROM THE PAGE: FIRST P
# Using the page that you already navigated to, use .locator("p"). This will
# find the location of all "p" elements in the page. Then use .nth(0) to get
# the first occurence of a "p" element. Then use .text_content() and print out
# the result to see what the first "p" element is.

    all_p_elements = page.locator("p")
    print(all_p_elements.nth(0).text_content())

# 3. VIEW CONTENT FROM ALL P ELEMENTS
# Do the same as #2, but this time, after getting all of the "p" elements using
# .locator(), use .count() to get the number of p elements it found. Then use
# a for loop with the .count() in a range to loop through each p element and
# print out the text in each. Put an extra space between each as you print it.

    all_p_elements = page.locator("p")
    print(all_p_elements.count())
    for index in range(all_p_elements.count()):
        print(index, all_p_elements.nth(index).text_content(), "\n")

    # for index in range(all_p_elements.count()):
    #     print(index, all_p_elements.nth(index).inner_text(), "\n")

# 4. FIND A SPECIFIC ELEMENT
# Let's say we want to grab the div that has the attribute of
# "product_description". We can use locator, but combine it with some extra
# instructions, like: .locator("div[id='product_description]")
    specific_div = page.locator("div[id='product_description']").text_content()
    print(specific_div)


# 5. FIND ELEMENTS NESTED IN OTHER ELEMENTS
# Let's say you want to find the the UPC id for the book. You might notice that
# it is in a <tr> element with no unique attributes to locate it. A good way
# to grab something and make it more robust is to find an element above the 
# element you want that you can more specifically locate with an attribute, then
# grab the nested element after that. Try grabbing the table with a class of
# "table table-striped" then the first tr inside the table, then the first td

    specific_cell = page.locator("table[class='table table-striped'] tr").nth(0).locator("td").nth(0)
    print(specific_cell.inner_text())

# 6. GRAB THE VALUE OF AN ATTRIBUTE
# Sometimes we want to grab data that is in the HTML attributes, not the content
# visible on the page. You can do this using .get_attribute() once you've found
# a single element. Let's grab the <ul> element with teh class of "breadcrumb"
# then get the value of the "href" attribute of the 3rd <a> element

    breadcrumb_ul = page.locator("ul[class='breadcrumb'] a").nth(2)
    href_attribute = breadcrumb_ul.get_attribute("href")
    print(href_attribute)


# 7. NAVIGATE TO A NEW PAGE
# You could use the href attribute that you pulled from the element in #6 to
# navigate to a new page. But, since we are using playwright, we can actually
# just directly control the browser. Tell it to click on the element you grabbed
# earlier using .click(). You can also use .fill() or .type() to enter text if
# that is ever needed.

    breadcrumb_ul.click()

