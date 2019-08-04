import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup as bs
import xml.etree.ElementTree as et

url = "http://py4e-data.dr-chuck.net/comments_265053.xml"
HtmlData = urllib.request.urlopen(url).read()
soup = bs(HtmlData, 'xml')      # 'xtml' is a fixed parameter.

treeData = et.fromstring(str(soup))     # Use str() to transfer the beautifulsoup object into string.
list = treeData.findall('comments/comment')

sum = 0
for each in list:
    newNumber = float(each.find('count').text)
    sum = sum + newNumber

print(sum)
