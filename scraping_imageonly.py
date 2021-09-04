
import requests
from bs4  import BeautifulSoup as soup
import html5lib

import wget

url ="https://www.imdb.com/list/ls053501318/"                 ## website URL 
r = requests.get(url)                               
htmlContent = r.content

bsobj = soup(htmlContent , "html.parser")                      ##parse the content


for img in bsobj.find_all('img'):                  # find all img file in content
    #print(item['src'])
    image = img.get('src')
    image_filename = wget.download(image) 
    
