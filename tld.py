# Scope is to find Top Level Domains ffrom wiki page
import requests
from urllib.parse import urlparse

from bs4 import BeautifulSoup

url = "https://en.m.wikipedia.org/wiki/List_of_Internet_top-level_domainsLinks"

response = requests.get(url=url)
tld_soup = BeautifulSoup(response.content, "html.parser")

# links = tld_soup.find_all('a')
# for link in links:
#     href = link.get("href")
#     print(href)
#     if urlparse(href).hostname is not None:
#         print(href)

tables = tld_soup.find_all('table')
for table in tables:
    tr = table.find_all('tr')
    print(dir(tr))
    tdlist = tr.find_all('td')
    print(tr.pop)
