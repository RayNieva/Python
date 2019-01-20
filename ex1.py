#!/usr/bin/env python
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
logging.debug('Start of program')


def printSomething():
    

    print("Hello World!")
    print("Hello Again")
    print("I like typing this.")
    print("This is fun.")
    print('Yay! Printing.')
    print("I'd much rather you 'not'.")
    print('I "said" do not touch this.')
    
    print('Another Line')



def main():
    printSomething()
    
if __name__ == '__main__':
    main()
    logging.debug('End of program')

