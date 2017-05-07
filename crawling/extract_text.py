from sys import argv
from bs4 import BeautifulSoup

_, arg1 = argv
print(arg1)
arq = open(arg1,'r')
html = arq.read()
soup = BeautifulSoup(html,'lxml')
for para in soup.find_all('p'):
    print(para.text)