
# Importing BeautifulSoup and 
# it is in the bs4 module
from bs4 import * 
import codecs
  
# Opening the html file. If the file
# is present in different location, 
# exact location need to be mentioned
HTMLFileToBeOpened = codecs.open("comments.html", "r", "utf-8") # use codecs.open to open html files!
  
# Reading the file and storing in a variable
contents = HTMLFileToBeOpened.read()
  
# Creating a BeautifulSoup object and
# specifying the parser 
soup = BeautifulSoup(contents, 'lxml')


# comments_dict = {'comments':[], 'timestamp':[]}
comments_list = []

# OLD METHOD
# USE div.class.class for multiple classes
# comments_div = 'div._2pin'
# timestamp_div = 'div._3-94'

# for text in soup.select(comments_div):
#     # print(text.string)
#     comments_dict['comments'].append(text.string)

# for timestamp in soup.select(timestamp_div):
#     # print(timestamp.string)
#     comments_dict['timestamp'].append(timestamp.string)

# print(comments_dict)


# NEW METHOD
for content in soup.find_all("div", class_="pam"): # content div of each comment
    # print(content,'\n')

    content_dict = {} # create a dictionary for each comment section
    content_dict['user'] = '41' # create 41 as user id
    content_dict['comment'] = content.find("div", class_="_2pin").get_text() if content.find("div", class_="_2pin") else "None" # comments text
    content_dict['timestamp'] = content.find("div", class_="_3-94").get_text() # comments timestamp

    comments_list.append(content_dict)

for i in comments_list:
    print(i,'\n')