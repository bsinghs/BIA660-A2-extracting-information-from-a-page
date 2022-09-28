# Scope is to find Top Level Domains ffrom wiki page
import requests
import parser
from bs4 import BeautifulSoup

url = "https://en.m.wikipedia.org/wiki/List_of_Internet_top-level_domainsLinks"

response = requests.get(url=url)
tld_soup = BeautifulSoup(response.content, "html.parser")
links = tld_soup.find_all('a')

for link in links:
    href = link.get("href")
    print(href)

