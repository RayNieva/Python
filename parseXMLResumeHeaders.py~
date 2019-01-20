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




def subheaderRegex():
    
    
    # TODO: Find subheaders extracting out text
    possibleSubheaderRegex=re.compile(r'<subheader.*</subheader>')
   
    
    text = str(pyperclip.paste())
    
    matches=[]
    

    subheaders=possibleSubheaderRegex.findall('*** This more text<subheaders>This is a test</subheader>')
    print(subheaders)
    pp=pprint.PrettyPrinter(indent=2)
    subheaders2=possibleSubheaderRegex.findall(text)
    #pp.pprint(subheaders2)

    for subhd in subheaders2:
        #print("*")
        subheader=etree.XML(subhd)
        pp.pprint(etree.tostring(subheader))


    
def main():
    subheaderRegex()
    logging.debug('End of program')


if __name__ == '__main__':
    main()

