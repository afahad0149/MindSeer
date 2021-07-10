
# Importing BeautifulSoup and 
# it is in the bs4 module
from bs4 import * 
import codecs
  
# Opening the html file. If the file
# is present in different location, 
# exact location need to be mentioned
HTMLFileToBeOpened = codecs.open("your_posts_and_comments_in_groups.html", "r", "utf-8") # use codecs.open to open html files!
  
# Reading the file and storing in a variable
contents = HTMLFileToBeOpened.read()
  
# Creating a BeautifulSoup object and
# specifying the parser 
soup = BeautifulSoup(contents, 'lxml')


group_comments_list = []
posts_list = []
substring_group = 'Group:'

for content in soup.find_all("div", class_="pam"): # content div of each comment
    # print(content,'\n')
    text = content.find("div", class_="_2pin").get_text() if content.find("div", class_="_2pin") else "None" # post text
    
    content_dict = {} # create a dictionary for each comment section
    content_dict['user'] = '41' # create 41 as user id
    content_dict['post'] = content.find("div", class_="_2pin").get_text() if content.find("div", class_="_2pin") else "None" # post text
    content_dict['timestamp'] = content.find("div", class_="_3-94").get_text() # comments timestamp

    if substring_group in text: # if its a group comment
        # print('group')
        group_comments_list.append(content_dict)
    else:
        # print('NOT group')
        posts_list.append(content_dict)


for i in group_comments_list:
    print(i,'\n')

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
for i in posts_list:
    print(i,'\n')