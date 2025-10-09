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
Basically everything you need to do with scraping can be accomplished with
four methods: 

    - .find('element_name', attrs={'attribute_name' : 'attribute_value'})
        - This finds the first occurence of an element within the html soup that you run it on.
        - So if you run it on the whole page, it will find the first element you specify,
            but if you run it on a subset of the html, it will find the first element you specify in that subset

    - .find_all('element_name', attrs={'attribute_name' : 'attribute_value'})
        - same as .find but gets all the elements within the html soup that you run it on, not just the first.
        - it returns a list, so you either need to loop through the list, or access a specific thing you want like list[2] to get the 3rd thing, etc.

    - .get_text()
        - grabs all the text from whatever html is contained in a soup object. Could be a single element, or multiple elements

    - .get('attribute_name')
        - gets the value of an attribute.
        so if you have <p class="example text">  and you did .get('class') it would return "example text"

'''

# Now, let's practice together, using the main page:
# https://books.toscrape.com/index.html


# Store the response object of the url above and create beautifulsoup object
response = requests.get("https://books.toscrape.com/index.html")
soup = BeautifulSoup(response.content, "html.parser")


# .find() and .get_text() practice
# print the price of the first book shown:

first_book_price = soup.find('p', attrs={'class' : 'price_color'})
text = first_book_price.get_text()
print(text)


# .find_all() and .get_text() practice
# print the price of all the books on the first page:
all_books_price = soup.find_all('p', attrs={'class' : 'price_color'})

for index, book_price_element in enumerate(all_books_price, start=1):
    text = book_price_element.get_text()
    print(f"Book {index}: {text}")


# .get() practice
# print out the url of every book on the first page
# Note that you can click on the image of the book, or on the book title. That means the urls are in at least 2 places
# There are a few different ways you could do this, which is the case for most webpages.

all_img_container_divs = soup.find_all('div', attrs={'class': 'image_container'})
for div_container in all_img_container_divs:
    url_text = "https://books.toscrape.com/" + div_container.find('a').get('href')
    print(url_text)

# Look at the urls you've scraped. Notice they are leaving out the domain name (the part of the url with a .com or .org, etc.)
# change it so that the url prints out the entire url, not just the relative path of it.

