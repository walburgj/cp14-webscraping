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
    #print(book_title)


# this is method 1, checking if an element is None

next_button_present = True
url = "https://books.toscrape.com/catalogue/page-48.html"
while next_button_present:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    print(f"current URL is: {url}")
    all_img_container_divs = soup.find_all('div', attrs={'class': 'image_container'})
    for div_container in all_img_container_divs:
        book_title = div_container.find('img').get('alt')
        print(book_title)

    # try to find the 'next button':
    next_button = soup.find('li', attrs={'class' : 'next'})

    if next_button:
        url = "https://books.toscrape.com/catalogue/" + next_button.find('a').get('href')
    else:
        next_button_present = False
        print("You are already at the last page")


# this is method 2, manually manipulating the url and checkign if it is valid.

current_page_number = 48
while True:
    url = f"https://books.toscrape.com/catalogue/page-{current_page_number}.html"
    response = requests.get(url)

    current_page_number +=1
    if response.status_code == 404:
        print(f"url: {url} \nNot a valid url. Stopping the loop")
        break

    soup = BeautifulSoup(response.content, "html.parser")
    print(f"current URL is: {url}")
    all_img_container_divs = soup.find_all('div', attrs={'class': 'image_container'})
    for div_container in all_img_container_divs:
        book_title = div_container.find('img').get('alt')
        print(book_title)





    