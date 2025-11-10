from helper_functions import clear_screen
clear_screen()

# ============================
# INSTALLING PACKAGES WITH PIP
# ============================

'''
In the terminal, run:
    pip install playwright
then, run this:
    playwright install
'''

from playwright.sync_api import sync_playwright
print("If this prints, that means you installed the playwright package correctly")
with sync_playwright() as p:
    p.chromium.launch() 

print("If this prints, that means you ran 'playwright install' in the terminal correctly")


