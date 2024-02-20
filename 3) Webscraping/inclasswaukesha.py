# pip install beautifulsoup4
# pip install requests

# import module
import requests
import bs4

# Generate the URL
url = "https://www.fox6now.com/tag/us/wi/waukesha-county"

# get the web page
request_result = requests.get(url).text

# print(request_result)

# parse the html
soup = bs4.BeautifulSoup(request_result, "html.parser")

# Find the articles and then we can extract the titles
temp = soup.find_all("article", class_="post")

##for i in temp:
##    x = i.find('div', class_="info")
##    header = x.find('header')
##    h3 = header.find('h3')
##    atag = h3.find('a')
##    print(atag.text)

for i in temp:
    x = i.find('div', class_="info")
    pinfo = x.find('p')
    ptext = pinfo.text
    print(ptext)
    print()
