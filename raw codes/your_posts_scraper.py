
# Importing BeautifulSoup and 
# it is in the bs4 module
from bs4 import * 
import codecs
  
# Opening the html file. If the file
# is present in different location, 
# exact location need to be mentioned
HTMLFileToBeOpened = codecs.open("your_posts_1.html", "r", "utf-8") # use codecs.open to open html files!
  
# Reading the file and storing in a variable
contents = HTMLFileToBeOpened.read()
  
# Creating a BeautifulSoup object and
# specifying the parser 
soup = BeautifulSoup(contents, 'lxml')


posts_list = []

for content in soup.find_all("div", class_="pam"): # content div of each comment
    # print(content,'\n')

    content_dict = {} # create a dictionary for each comment section
    content_dict['user'] = '41' # create 41 as user id
    content_dict['post'] = content.find("div", class_="_3-95").get_text() if content.find("div", class_="_3-95") else "None" # post text
    content_dict['timestamp'] = content.find("div", class_="_3-94").get_text() # comments timestamp

    posts_list.append(content_dict)

for i in posts_list:
    print(i,'\n')