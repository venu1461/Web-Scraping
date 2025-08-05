# it's find out the which is previous sibling for 'ul' 
import requests
import bs4
file_path='C:/Users/91730/Desktop/python/newthings/index.html'
with open(file_path,'r') as f:
    html_content=f.read()
soup=bs4.BeautifulSoup(html_content,'html.parser')
parent_li=soup.ul.previous_siblings
for ele in parent_li:
    if ele !='\n':
        print(ele)