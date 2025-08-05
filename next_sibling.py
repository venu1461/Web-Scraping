# it's find out the next_sibling of 'h1'
import requests
import bs4
file_path='C:/Users/91730/Desktop/python/newthings/index.html'
with open(file_path,'r') as f:
    html_content=f.read()
soup=bs4.BeautifulSoup(html_content,'html.parser')
parent_li=soup.h1.next_sibling.next_sibling
# for ele in parent_li:
#     print(ele.name)
print(parent_li)