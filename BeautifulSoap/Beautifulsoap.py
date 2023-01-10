from bs4 import BeautifulSoup
content = """
<html><head><title>Geeks For Geeks</title></head>
<body>
<p class="title"><b>most viewed courses in GFG,its all free</b></p>
<p class ="prog">Top 5 Popular Programming Languages</p>
<a href="https://www.geeksforgeeks.org/java-programming-examples/"class="prog" id="link1">Java</a>

<a href="https://www.geeksforgeeks.org/cc-programs/" class="prog" id="link2">c/c++</a>

<a href="https://www.geeksforgeeks.org/python-programming-examples/" class="prog" id="link3">Python</a>
<a href="https://https://www.geeksforgeeks.org/introduction-to-javascript/"class="prog" id="link4">Javascript</a>
<a href="https://www.geeksforgeeks.org/ruby-programming-language/" class="prog" id="link5">Ruby</a>
<p>according to an online survey. </p>
<p class="prog"> Programming Languages</p>
</body></html> """

soup = BeautifulSoup(content,'html.parser')
# print(soup.head)
# print(soup.a)
# print(soup.find_all("a"))
# print(soup.head.contents,'@@@@')

# print(soup.head.children,'*****')

# for child in soup.body.descendants:
#     print(child,'1')

for string in soup.strings :
    print(repr(string))