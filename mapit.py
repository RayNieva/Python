#!/usr/bin/env python

#! python3
# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard.



import logging, webbrowser, sys

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')

logging.debug('Start of program')

def mapit():
    


    if len(sys.argv) > 1:
        # Get address from command line.
        address = ' '.join(sys.argv[1:])
        logging.debug(sys.argv)
        logging.debug(address)
    
    else:
        # Get address from clipboard.
        address = pyperclip.paste()
        logging.debug(address)
    
    webbrowser.open('https://www.google.com/maps/place/' + address)

def main():
    mapit()
    logging.debug('End of program')


if __name__ == '__main__':
    main()
