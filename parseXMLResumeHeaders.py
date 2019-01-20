#!/usr/bin/env python

#! python3


# parsesXMLResumeSubheader.py - Finds and returns XML Subheaders on the clipboard.

import pyperclip, re, logging, pprint
from lxml import etree


logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')

logging.debug('Start of program')

""">>> root = etree.XML("<root>data</root>")
>>> print(root.tag)
root
>>> etree.tostring(root)
b'<root>data</root>"""




def headerRegex():
    
    
    # TODO: Find headers extracting out text
    possibleHeaderRegex=re.compile(r'<header.*</header>.*', re.DOTALL)
   
    
    text = str(pyperclip.paste())
    
    matches=[]
    

    headers=possibleHeaderRegex.findall('*** This more text<header>This is a test</header>')
    print(headers)
    pp=pprint.PrettyPrinter(indent=2)
    headers2=possibleHeaderRegex.findall(text)
    pp.pprint(headers2)

    """
    for hdr in headers2:
        #print("*")
        header=etree.XML(hdr)
        pp.pprint(etree.tostring(header))"""


    
def main():
    headerRegex()
    logging.debug('End of program')


if __name__ == '__main__':
    main()

