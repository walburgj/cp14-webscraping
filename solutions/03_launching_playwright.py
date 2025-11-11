from helper_functions import clear_screen
clear_screen()

# ====================
# LAUNCHING PLAYWRIGHT
# ====================

'''
OVERVIEW
--------
Playwright launches a web browser and maintains a connection from the web
browser to your python code. That makes it great for web scraping and automating
tasks in a web browser. Web scraping just means grabbing data from websites.

To practice, we are going to use this webscraping practice site:
https://books.toscrape.com/catalogue/page-2.html

'''

# 1. IMPORT THE SYNC API FROM PLAYWRIGHT
'''
At the top of your page, make sure you add this:

from playwright.sync_api import sync_playwright

If you want to get fancy in the future, you can loop up the async api, but 
that requires knowledge beyond what we cover in this class.
'''

from playwright.sync_api import sync_playwright


# 2. CREATE CONTEXT MANAGER AND LAUNCH A BROWSER
'''
With playwright, you need to launch a browser and connect to it, and make sure
the browser automatically shuts down when you are done with it. You use the 
python keyword "with" to start up a context manager (and in this case the
context is the web browser controlled by playwright). 

Indented from the context manager, you launch a browser, give that browser a 
context (like the cache and cookies that your browser has acccess to), and then
you load up a new page.

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=3000) # getting the chromium browser
    context = browser.new_context() # no shared cache/cookies in the chromium broswer
    page = context.new_page() # load a new page using that new context


'''
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=3000) # getting the chromium browser
    context = browser.new_context() # no shared cache/cookies in the chromium broswer
    page = context.new_page() # load a new page using that new context

    page.goto("https://books.toscrape.com/catalogue/page-2.html")
    print(page.title())
    print(page.content())

    input("Press enter to end")


# 3. GO TO A SPECIFIC PAGE
'''
Still indented from the "with" context manager, use the page you made and use
.goto() and go to this site:
    https://books.toscrape.com/catalogue/aladdin-and-his-wonderful-lamp_973/index.html

Then, print out the .title() and .content() in python. See what you get.
You can put an input("press enter to end") after everything so that the website
doesn't close if you want.
'''