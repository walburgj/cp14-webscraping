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
A common practice in websraping is looping through a list of URLs
and loading those individual pages and then scraping those

'''

# Store the response object, create beautifulsoup object
response = requests.get("https://books.toscrape.com/index.html")
soup = BeautifulSoup(response.content, "html.parser")

# You may have written this differently, but this code grabs all the urls
# on the first page of Books to Scrape
# alter the code so that instead of printing it out, it stores the urls in
# a list called "list_of_urls"
all_img_container_divs = soup.find_all('div', attrs={'class': 'image_container'})
for div_container in all_img_container_divs:
    url_text = "https://books.toscrape.com/" + div_container.find('a').get('href')
    print(url_text)

# here's my finished version:
list_of_urls = []
all_img_container_divs = soup.find_all('div', attrs={'class': 'image_container'})
for div_container in all_img_container_divs:
    url_text = "https://books.toscrape.com/" + div_container.find('a').get('href')
    list_of_urls.append(url_text)

# now, loop through your list of urls
# in each iteration, request the url and get a new soup object for that page.
# print out "requesting url: then the url"
# I want you to print out the Title, UPC, and Tax from the page of each book you loop through like this:
# "Title: Example, UPC:ab34lj52hlskjp3532, Tax: 20"

for url in list_of_urls:
    if 'the' in list_of_urls:
        continue
    print(f"requesting url: {url}")
    response = requests.get(url)
    specific_page_soup = BeautifulSoup(response.content, "html.parser")
    title = specific_page_soup.find('h1').get_text()
    table_cells = specific_page_soup.find_all('td')
    upc = table_cells[0].get_text()
    tax = table_cells[4].get_text()
    the_count = specific_page_soup.get_text().lower().count('the')

    print(f"Title: {title}, UPC: {upc}, Tax: {tax}, count of 'the': {the_count}")


# it is often the case that there are specific urls you don't want to visit
# see if you can change your code so that you don't visit the page for any book that has "the" in it.

'''
You could either check for it before you add it to your list of urls, or check for it while looping through the list.
'''

# now, try printing a count of how many times "the" or "The" appears on the whole page.
# you can use .count() on any string to count how many times a sub string appears in it.
# note, this will count instances like "there". If you are interested in leaving out cases like that,
# read up on regular expressions. We don't have time to delve into it in this class.
