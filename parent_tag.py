# find out the childrens for tags
import requests
import bs4
file_path='C:/Users/91730/Desktop/python/newthings/index.html'
with open(file_path,'r')as f:
    html_content=f.read()
soup=bs4.BeautifulSoup(html_content,'html.parser')
next_content=soup.li.parent
print(next_content.name)