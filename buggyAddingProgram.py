#!/usr/bin/env python

import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
logging.debug('Start of program')

def buggyAdder():
    

    print('Enter the first number to add:')
    first=input()
    first=int(first)
    assert first==int(first), first + ' Needs conversion to integer'

    print('Enter the second number to add:')
    second=input()
    second=int(second)
    assert second==int(second), second + ' Needs conversion to integer'
    
    print('Enter the third number to add:')
    third=input()
    third=int(third)
    assert third==int(third), third + ' Needs conversion to integer'

    total=first + second + third
    assert total==int(total), 'If string needs conversion to integer'
    
    #print('The sum is ' + str(first) + str(second) + str(third)) what was happening
    total=str(total)
    assert total==str(total), total + ' needs converstion to string before printing output'
    print('The sum is ' + total)
    

def main():
    logging.debug('Entering main')
    buggyAdder()

if __name__ == '__main__':
    main()
    logging.debug('End of program')

