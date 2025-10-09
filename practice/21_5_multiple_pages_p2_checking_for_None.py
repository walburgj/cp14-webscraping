# optional stuff that will clear the window each time you run it.
import os
import platform

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

clear_screen()

###########################
# START READING HERE
###########################

from bs4 import BeautifulSoup
import requests

'''
Let's start at page 48 this time.
Notice it has a "next" button on the bottom of the page. But page 50 doesn't

you can either:
    - look for the next button, and if it returns None, exit the process
    - manipulate the url, check if the response.status_code == 404 and exit if it does

'''

# This code is starting on page 48 and printing all the titles of the books. 
# I want you to alter this code so that it will keep going to more pages until there aren't any
# if it realizes there are no more pages, print ("You are already at the last page")

response = requests.get("https://books.toscrape.com/catalogue/page-48.html")
soup = BeautifulSoup(response.content, "html.parser")

all_img_container_divs = soup.find_all('div', attrs={'class': 'image_container'})
for div_container in all_img_container_divs:
    book_title = div_container.find('img').get('alt')
    print(book_title)





    