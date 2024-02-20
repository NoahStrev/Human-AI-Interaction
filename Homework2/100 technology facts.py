from bs4 import BeautifulSoup
import requests

url ='https://www.thefactsite.com/top-100-technology-facts'
request_result = requests.get(url).text
soup = BeautifulSoup(request_result, "html.parser")
text = soup.get_text()
rawtext = "".join([s for s in text.strip().splitlines(True) if s.strip("<br/>").strip()])
print(rawtext)
