from bs4 import BeautifulSoup
import requests


# 1.step1 :Get The HTML
r = requests.get(" https://www.codewithharry.com/")

# 2.Get the page content
Htmlcontent = r.text
# print(Htmlcontent)

# 3.Parse the HTML:
soup = BeautifulSoup(Htmlcontent,'html.parser')
print(type(soup))
# print(soup.prettify)

title=soup.title
# print(title,'@@@***')

# paras=soup.find_all("p")
# print(paras,'*********')



