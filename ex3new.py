#!/usr/bin/env python

import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')

logging.debug('Start of program')

def funWithMath():
    


    print("I will now count my chickens:")
    
    print("Hens", 25.0 + 30.0/6.0)
    
    print("Roosters",  100.0 - 25.0 * 3.0 % 4.0)
    
    print("Now I will count the eggs:")
    
    print(3.0+2.0+1.0-5.0+4.0%2.0-1.0/4.0+6.0)
    
    print("Is it true that 3+2<5-7?")
    
    print(3.0+2.0<4.0-7.0)
    
    print("what is 3+2?", 3.0+2.0)
    
    print("What is 5-7", 5.0-7.0)
    
    print("Oh, that's why it's False.")
    
    print("How about some more.")
    
    print("Is it greater?", 5.0 > -2.0)
    
    print("Is it greater or equal?", 5.0 >= -2.0)
    
    print("Is it less or equal?", 5.0<=-2.0, "I don't know!")



def main():
    funWithMath()

if __name__ == '__main__':
    main()
    logging.debug('End of program')
