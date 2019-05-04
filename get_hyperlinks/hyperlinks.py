# Import libraries
from bs4 import BeautifulSoup
import re as regex
import requests


def get_redirects(url):
    '''
    take in link
    create dictionary object to hold a tag text and href links
    a tag will be key
    href will be value
    loop through 
    Using regular expressions, gather text between a tags
    Add a tag text as key
    Add the href as value
    return dictionary
    '''
    redirects = {}
    page = requests.get(url)
    html_text = page.text
    html = BeautifulSoup(html_text, features="html.parser")

    for link in html.find_all('a', href=True):       
        redirects[link.string] = link['href']

    return redirects

# Gather url input
print('Enter Url', end=': ')
url = input()
print()

# Call functions to gather data
redirect_dictionary = get_redirects(url)

# Print data

# Hyperlinks
print('Hyperlink Text and their URL Counterparts:')
for link in redirect_dictionary:
    print(str(link) + ': ' + str(redirect_dictionary[link]))
print()



