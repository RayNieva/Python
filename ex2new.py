#!/usr/bin/env python

import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')

logging.debug('Start of program')

def printSomeMore():
    

    # A comment, this is so you can read your program later.
    # Anything after the # is ignored by python.
    
    print("I could have code like this.") # and the comment after is ignored
    
    # You can also use a comment to "disable" or comment out code:
    # print("This won't run.")
    
    print("This will run.")
    
    print('This will run too.')
    
    toPrint="""Take your ex2.py file and review each line going backward. Start at the last line, and check each word in reverse against what you should have typed."""
    
    print(toPrint)




def main():
    printSomeMore()
    

if __name__ == '__main__':
    main()
    logging.debug('End of program')
