from typing import Container
import requests
from bs4  import BeautifulSoup as soup
import html5lib
import os
import urllib.request
import wget

url ="https://www.imdb.com/list/ls053501318/"                 ## website URL 
r = requests.get(url)                               
htmlContent = r.content

bsobj = soup(htmlContent , "html.parser")                      ##parse the content
#print(bsobj.prettify())

containers = bsobj.find_all('div',{'class':'lister-item mode-detail'})      ## location of image and name 
print(containers)

pic = bsobj.find_all('img')                           # find all img file in content

#print(pic)

for container,img in zip(containers,pic):#zip function takes 0 index from  list 1 and index 0 from 2nd list and then combine it
    name = container.h3.a.text.strip()   # conatainer /h3/a go there and take text and save in name vairable

    #print(name)
    image = img.get('src')              ## gett image URL from SRC 
   # print(image)

    full_name = str(name) + ".jpg"           ## save file name  plus JPG
    image_filename = wget.download(image,full_name)     ## wget function is use for downloading
    #urllib.request.urlretrieve(image, full_name)        ## URLlib also used for downlaoding



