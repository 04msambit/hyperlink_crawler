import urllib2
from BeautifulSoup import BeautifulSoup
import re
import json


total = 0
while total < 1000:
      page = urllib2.urlopen("http://rivermeadow.com")
      soup = BeautifulSoup(page)
      print len(soup.findAll('a',{'href': True}) )
      total += len(soup.findAll('a',{'href': True}) )

      for incident in soup.findAll('a',{'href': True}):
          
          print incident['href']
          if 'http' in str(incident['href']):
              url_string = str(incident['href'])
              page = urllib2.urlopen(url_string)
              soup = BeautifulSoup(page)
              print len(soup.findAll('a',{'href': True}) )
              total += len(soup.findAll('a',{'href': True}) )


print total    
