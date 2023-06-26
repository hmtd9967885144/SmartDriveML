import requests
import collections
collections.Callable = collections.abc.Callable
from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate


website_url = requests.get('https://learn.microsoft.com/en-us/azure/architecture/aws-professional/services').text
soup = BeautifulSoup(website_url,'lxml')
soup = BeautifulSoup(website_url, 'html.parser')

for table in soup.find_all('table'):
    # count = count+1
    # if count==3:
    text_file = open("Test_html.html.", "w")
    text_file.write(str(table))
    text_file.close()
    tbl = pd.read_html('Test_html.html')[0]
    print(tabulate(tbl, headers='keys', tablefmt='psql'))
        #break

# tbl = pd.read_html('Test_html.html')[0]
# print(tabulate(tbl, headers='keys', tablefmt='psql'))
