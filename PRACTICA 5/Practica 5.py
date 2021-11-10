import requests
from bs4 import BeautifulSoup

url = "https://cybersecuritynews.es/network-security/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

blog_titles = soup.findAll('h1', attrs={"class":"elementor-heading-title elementor-size-default"})
for title in blog_titles:
    print(title.text)

f = open("bs.txt","w")
for title in blog_titles:
    f.write(title.text)
f.close()
