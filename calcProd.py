#!/usr/bin/env python
import logging, time

#calcProd.py Calculating Time

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')



logging.debug('Start of program')

def calcProd():
    # Calculate the product of the first 100,000 numbers.
    product = 1
    for i in range(1, 100000):
        product = product * i
    return product



def callCalcProd():
    

    startTime = time.time()
    logging.debug('The start time is ' + str(startTime))
    prod = calcProd()
    endTime = time.time()
    logging.debug('The end time is ' + str(endTime))
    print('The result is %s digits long.' % (len(str(prod))))
    print('Took %s seconds to calculate.' % (endTime - startTime))





def main():
    callCalcProd()
    logging.debug('End of program')

if __name__ == '__main__':
    main()
