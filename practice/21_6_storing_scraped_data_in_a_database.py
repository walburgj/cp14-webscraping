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
import pandas as pd
import sqlalchemy

# define the connection parameters:
database_name = "is303"
db_user = "is303user"
db_password = "12345classpassword"
db_host = "localhost" #this just means the database is stored on your own computer
db_port = "5432" # default setting

# Connect to the PostgreSQL database
engine = sqlalchemy.create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{database_name}')



response = requests.get("https://books.toscrape.com/catalogue/page-48.html")
soup = BeautifulSoup(response.content, "html.parser")

'''
In this example, we are going to loop through all the books, and store the
book title and price as each row in a database.

One relatively simple way to do this, is to create a dictionary for storing the
Title and the Price, converting that dictionary into a dataframe for each row
and then appending that to sql.

'''

