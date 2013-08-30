import urllib2
from BeautifulSoup import BeautifulSoup
import re
import json


total = 0
list_url=[]


def obtain_json():

    count=0    

    populate_list("http://rivermeadow.com")

    while len(list_url) < 1000:
      populate_list(list_url[count])
      count+=1
                     

def populate_list(url):
    
    print url
    global list_url
    

    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page)

    for incident in soup.findAll('a',{'href': True}):
        if 'http' in str(incident['href']):
            list_url.append(str(incident['href']))

def main():
    global list_url
    obtain_json()
    print list_url
    
if __name__ == '__main__':
  main() 
