#!/usr/bin/env python
# This is the requestTemplate.py  Example using the requests module to download pages from a website.

import logging, os, requests, subprocess

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')

logging.debug('Start of program')

#import requests
"""
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
type(res)
res.status_code==requests.codes.ok
len(res.text)
print(res.text[:250])
res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
res.raise_for_status()
"""

def getRES():
    


    # Downloads text file from web
    res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
    res.raise_for_status()
    
    #import os
    #os.getcwd()
    
    playFile = open('RomeoAndJuliet.txt', 'wb')
    
    for chunk in res.iter_content(100000):
            playFile.write(chunk)
    playFile.close()
    print('The current working directory is ' + os.getcwd())
    subprocess.call(['cat','RomeoAndJuliet.txt'])



def main():
    getRES()
    logging.debug('End of program')


if __name__ == '__main__':
    main()
