#!/usr/bin/env python

#This is the sample lesson program for Beautiful Soup


import logging, bs4, requests

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')

logging.debug('Start of program')


def exampleSoup():
    


    res = requests.get('http://nostarch.com')
    res.raise_for_status()
    noStarchSoup=bs4.BeautifulSoup(res.text, features="html5lib")
    type(noStarchSoup)
    exampleFile=open('example.html')
    exampleSoup=bs4.BeautifulSoup(exampleFile,features="html5lib")
    type(exampleSoup)
    logging.debug(type(exampleSoup))
    
    elems=exampleSoup.select('#author')
    type(elems)
    logging.debug(type(elems))
    
    len(elems)
    logging.debug('Is length of list: ' + str(len(elems)))
    
    type(elems[0])
    logging.debug(type(elems[0]))
    
    elems[0].getText()
    logging.debug(elems[0].getText())
    
    str(elems[0])
    logging.debug(str(elems[0]))
    
    elems[0].attrs
    logging.debug(elems[0].attrs)
    
    pElems = exampleSoup.select('p')
    str(pElems[0])
    logging.debug(str(pElems[0]))
    
    pElems[0].getText()
    logging.debug(pElems[0].getText())
    
    str(pElems[1])
    logging.debug(str(pElems[1]))
    
    pElems[1].getText()
    logging.debug(pElems[1].getText())
       
    str(pElems[2])
    logging.debug(str(pElems[2]))
       
    pElems[2].getText()
    logging.debug(pElems[2].getText())
   



def main():
    exampleSoup()
    logging.debug('End of program')

if __name__ == '__main__':
    main()
