import urllib2
from BeautifulSoup import BeautifulSoup
import re
import json
import sys
import json

total = 0
list_url=[]
dump_file=''


def obtain_json():

    count=0

    max_limit = sys.argv[4]
    initial_url = str(sys.argv[2])    

    populate_list(initial_url)

    while len(list_url) < max_limit:
      populate_list(list_url[count])
      count+=1
                     

def populate_list(url):
    
    try:    
    
      global list_url
      global dump_file
    

      page = urllib2.urlopen(url)
      soup = BeautifulSoup(page)

      for incident in soup.findAll('a',{'href': True}):
        try:
           if 'http' in str(incident['href']).encode('ascii','ignore'):
              list_url.append(str(incident['href']))
        except UnicodeEncodeError:
               print 'Test
 
      with open(dump_file, "w") as file:
        json.dump( {'url':url,'outgoing':list_url}, file, indent=4)
      file.close()

    except:
        print ''  



def read():

    with open(dump_file) as file:
       result = load(file)
    file.close()
    print (type(result))
    print (result.keys())
    print (result)
        


def main():
    
    global list_url
    global dump_file

    dump_file = str(sys.argv[6])    

    obtain_json()
    read()
    
    
if __name__ == '__main__':
  main() 
