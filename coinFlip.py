#!/usr/bin/env python

import random, logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
logging.debug('Start of program')
def coinFlip():
    

    heads=0
    for i in range(1, 1001):
        if random.randint(0, 1) == 1:
            heads = heads + 1
            if i == 500:
                print('Halfway done!')
    print('Heads came up ' + str(heads) + ' times.')
        


def main():
    coinFlip()

if __name__ == '__main__':
    main()
    logging.debug('End of program')

