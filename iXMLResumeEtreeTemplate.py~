#!/usr/bin/env python
import logging

from lxml import etree

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
logging.debug('Start of program')

def myTree():
    


    # create XML 
    root = etree.Element('root')
    root.append(etree.Element('child'))
    # another child with text
    child = etree.Element('child')
    child.text = 'some text'
    root.append(child)
    
    # pretty string
    s = etree.tostring(root, pretty_print=True)
    print (s)



def main():
    myTree()
    logging.debug('End of program')

if __name__ == '__main__':
    main()
