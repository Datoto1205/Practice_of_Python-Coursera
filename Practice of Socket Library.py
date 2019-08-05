# Use Socket to Fetch The HTML Code
print("\nUse Socket to Fetch The HTML Code\n")
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# This code is used to build the socket.

mysock.connect(('data.pr4e.org', 80))
# This code is used to use the socket we created to connect to the client server.
# 80 is the general port of fetching the sebsite.
# 'data.pr4e.org' is the socket here, we could change it in the future.
# Take "http://www.google.com.tw/otherfile.txt" for example, "http://" is protocal, "www.google.com.tw" is socket, and the rest part is the document.

cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# This code is used to compile the code of asking the data.
# Ths string we typed was formed by "unicode", while the server only know "byte", so we need to add encode() to transform the UTF-8 string into byte.
# The encode() method and decode() method would use UTF-8 as default coding form.
# The code above used HTTP protocal, and it seems that this code would fail if the protocal is not HTTP. Therefore, take into account other way to fetch the data...

mysock.send(cmd)
# This code is used to send our asking to the server.

while True:
    data = mysock.recv(512)
    # After the asking was sent out, we used recv() method to receive the feedback.
    if (len(data) < 1):
        break   # It means the feedback was nothing.
    print(data.decode())    # We need to decode so that we could know what's the content of the feedback.

mysock.close()
# This code is used to terminate the socket we built.



# Use Urllib to Fetch The HTML Code
print("\nUse Urllib to Fetch The HTML Code\n")
import urllib.request, urllib.parse, urllib.error   # Python 3 only, it seems that it could not work in Atom...

data = urllib.request.urlopen('https://www.google.com')     # Python 3 only, it seems that it could not work in Atom...

for j in data:
    print(j.decode().strip())
# Referred article 1: https://stackoverflow.com/questions/19729927/urllib-module-error-attributeerror-module-object-has-no-attribute-request?rq=1
# Referred article 2: https://stackoverflow.com/questions/35245430/httpresponse-object-has-no-attribute-decode



# Use Urllib & BeautifulSoup to Fetch The HTML Code
print("\nUse Urllib & BeautifulSoup to Fetch The HTML Code\n")
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup as bs

url = "https://www.google.com"
HtmlData = urllib.request.urlopen(url).read()
soup = bs(HtmlData, 'html.parser')      # 'html.parser' is a fixed parameter.
#print(soup)

tag = soup('a')     # Extract all the html code inside tage <a>.
for each in tag:
    print(each.get('href'))     # Extract each href within tag <a>.
