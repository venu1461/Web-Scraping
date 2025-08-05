# this code is used to find the anchor tags in the code
import requests
import bs4
file_path='C:/Users/91730/Desktop/python/newthings/index.html'
with open(file_path,'r')as f:
    html_content=f.read()
soup=bs4.BeautifulSoup(html_content,"html.parser")
anchor_tag=soup.a
print(anchor_tag['href'])
print(anchor_tag.attrs)