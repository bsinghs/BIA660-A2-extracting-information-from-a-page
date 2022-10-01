# BIA660-A2-extracting-information-from-a-page
Extracting information from a page

All of the top-level domains have been conveniently compiled into a list on Wikipedia: https://en.m.wikipedia.org/wiki/List_of_Internet_top-level_domainsLinks to an external site.

Goal

In this assignment, you will write a program that scapes the Wikipedia list of top-level domains and writes a CSV file that contains all the top-level domains and whether their "example" second-level domain resolves to an address that returns an HTTP responses.

Step 1

Use the Requests module to download the page with the list of top-level domains.

Step 2

Use BeautifulSoup, regular expressions, or some other means to extract the relevant domains.

Step 3

Use the Requests package to check whether the "example" second-level domain is valid for each of the top-level domains you extracted.

Step 4

Write a CSV file (https://docs.python.org/3/library/csv.htmlLinks to an external site.) with the results.

Step 5

Place your program in a GitHub Gist (see https://help.github.com/articles/creating-gists/ for instructions).

Step 6

Submit the URL of your Gist using Canvas.

Step 7

Submit your generated CSV file using Canvas.


_Steps are added as comments in the main script called tld.py._

_The script creates tlds.xlsx excel sheet with results._