#!/usr/bin/env python

import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')

logging.debug('Start of program')

def allCatNames():
    catNames=[]
    # Notice to keep things going, using a Loop
    while True:
        
        print('Enter the name of cat ' + str(len(catNames)+1) +  #Converting to a string to concatenate and print a number
              ' (Or enter nothing to stop.):')
        name=input()
        if name == '':
            break
        catNames=catNames+[name] #list concatenation
    print('The cat names are:')
    # Again to keep things going, using a For Loop to move thru a list
    for name in catNames:
        print('  '+ name) #The space indents the printed list
        
        
def main():
    allCatNames()
    


if __name__ == '__main__':
    main()
    logging.debug('End of program')
