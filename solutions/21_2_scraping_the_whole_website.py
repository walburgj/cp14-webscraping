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
web scraping just means extracting data from websites

You give your code a url to a website, it will download the html, and then you can
parse the exact parts of the html to grab what you want.
Then you can store it, analyze it, display it, whatever you want to do with the data you scraped.

We're going to be practicing with 
http://books.toscrape.com/

A great reference is the beautifulsoup documentation page:
https://beautiful-soup-4.readthedocs.io/en/latest/

'''

# Store the response object. use requests.get("url of website")
oResponse = requests.get("http://books.toscrape.com/")

# you can see a "status code" of your request using oResponse.status_code. 200 means it worked. Most common error is 404, or "not found"
print(oResponse.status_code)

# if you want to see the actual html code of the website, you can use oResponse.content
# less useful for our class (might come in handy if the website is giving you raw files instead of html)
# try printing it out.
print(oResponse.content)

# but we want the data in a form that is even easier to parse and extract data
# (parse means to analyze each piece or component of something. In this case we have a whole html file,
# but we probably only want to work with specific elements or tags.)

# we use beautifulsoup for this
# soup = BeautifulSoup(oResponse.content, "html.parser")
soup = BeautifulSoup(oResponse.content, "html.parser")

# this puts our html into a beautiful soup object, and we told it to assume that it is an html file that we can parse like a normal html file
# try printint out the soup variable you made
print(soup)

# you can also run the .prettify() method on the soup and print that out, it includes indents.
print(soup.prettify())