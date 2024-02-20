# pip install beautifulsoup4
# pip install requests

# import module
import requests
import bs4

# Generate the URL
url = "https://www.secondsale.com/author/james-patterson/359404/"

# get the web page
request_result = requests.get(url).text

# print(request_result)

# parse the html
soup = bs4.BeautifulSoup(request_result, "html.parser")

temp = soup.find_all("article", class_="product-miniature")

for i in temp:
    x = i.find('div', class_="product-description")
    pinfo = x.find('h1')
    ptext = pinfo.text.strip()
    print(ptext)
#    print()
