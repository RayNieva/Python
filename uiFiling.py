#!/usr/bin/env python
import logging, webbrowser, subprocess

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
logging.debug('Start of program')


def uiFile():


    commandList=["start","emacsc.bat"]
    logging.debug(commandList)
    subprocess.call(commandList)

    urlGML='https://gmail.com'
    urlLnk='https://www.linkedIn.com'
    urlUI='https://www.mass.gov/unemployment-insurance-ui-online'
    
    logging.debug(urlGML)
    logging.debug(urlLnk)
    logging.debug(urlUI)
    
    webbrowser.open(urlGML)
    webbrowser.open(urlLnk)
    webbrowser.open(urlUI)


def main():
    logging.debug('Entering main')
    uiFile()
    logging.debug('End of program')

if __name__ == '__main__':
    main()
