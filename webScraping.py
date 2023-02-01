
import requests
from bs4 import BeautifulSoup

#"-------------------------BUSINESS----------------------------------------"
# target url
url = 'https://www.cnn.com/business'
file1 = open("business.txt","w")
#requests instance
req = requests.get(url)

#parse html content
soup = BeautifulSoup(req.content,'html.parser')
file1.write((soup.title.string+"\n\n"))   #print title of the page
business_titles = soup.find_all('span',class_="cd__headline-text") #target the class using find_all method

#dump titles in a file called business.txt
for title in business_titles:
 file1.write((title.getText()))
 file1.write("\n")

file1.close()




#"----------------------------ENTERTAINMENT-------------------------------------"
url = 'https://www.cnn.com/entertainment'
file2 = open("entertainment.txt","w")

# make requests instance
req = requests.get(url)

soup = BeautifulSoup(req.content,'html.parser')
# print title
file2.write((soup.title.string+"\n\n")) 

entertainment_titles = soup.find_all('span',class_="cd__headline-text")   #target the spna tag and class using find_all method
#dump entertainment titles into file- entertainment.txt
for title in entertainment_titles:
 file2.write((title.getText()))
 file2.write("\n")
file2.close()




#"----------------------------STYLE-------------------------------------"
url = 'https://www.cnn.com/style'
file3 = open("style.txt","w")
# making requests instance
req = requests.get(url)

soup = BeautifulSoup(req.content,'html.parser')
file3.write((soup.title.string+"\n\n")) 
style_titles = soup.find_all('a',class_="CardBasic__title")
for title in style_titles:
 file3.write((title.getText()))
 file3.write("\n")

file3.close()
