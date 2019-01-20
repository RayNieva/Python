#!/usr/bin/env python

import logging
from selenium import webdriver



logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')

logging.debug('Start of program')



def seleniumWebDriverTemplate():
    

    browser = webdriver.Firefox()
    type(browser)
    browser.get('http://inventwithpython.com')
    browser.quit





def main():
    seleniumWebDriverTemplate()
    logging.debug('End of program')


if __name__ == '__main__':
    main()
