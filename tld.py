from dataclasses import replace
from os import link
import requests
from urllib.parse import urlparse
import re
import pandas as pd
from bs4 import BeautifulSoup

# This function checks whether a given url gives some response and returns corresponding result
def testurl(url):
    print("url: {}".format(url))
    try:
        response = requests.get(url=url)
        response_code = response.status_code
        print("response.status_code: {}".format(response_code))
        soup = BeautifulSoup(response.content, "html.parser")
        para = soup.find_all("p")
        output=para
    except:
        print("Error when running requests.get for {}".format(url) )
        response_code = "NOT AVAILABLE"
        output = "NOT AVAILABLE"
    return [url, response_code, output]

# This is the page with the list of top-level domains
url = "https://en.m.wikipedia.org/wiki/List_of_Internet_top-level_domains"

# Step 1: Use the Requests module to download the page with the list of top-level domains.
response = requests.get(url=url)
tld_soup = BeautifulSoup(response.content, "html.parser")
links = tld_soup.find_all('a')
all_rows = []

# Step 2: Use BeautifulSoup, regular expressions, or some other means to extract the relevant domains.
for link in links:
    href = link.get("href")
    parsed = urlparse(href)
    hostname = parsed.hostname
    match = re.fullmatch("\/wiki\/\.[A-Z,a-z]*", href)
    if match is not None:
        # Step 3: check whether the "example" second-level domain is valid for each of the top-level domains you extracted
        example_url = href.replace("/wiki/", "https://www.example")        
        row = testurl(example_url)
        all_rows.append(row)

# Step 4: Write a CSV file (https://docs.python.org/3/library/csv.htmlLinks to an external site.) with the results.
df = pd.DataFrame(all_rows,columns=["url", "response_code", "output"])
df.to_excel("tlds.xlsx")
