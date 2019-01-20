#!/usr/bin/env python
import logging, traceback

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')

logging.debug('Start of program')


def spam():
    logging.debug('spam calls bacon')
    bacon()
def bacon():
    logging.debug('bacon has try/except handling')
    try:
        raise Exception('This is the error message.')
    
    except Exception:
        
        errorFile = open('errorInfo.txt', 'w')
        errorFile.write(traceback.format_exc())
        errorFile.close()
        print('The traceback info was written to errorInfo.txt.')



#spam()



def main():
    logging.debug('Entering main')
    spam()

if __name__ == '__main__':
    main()
    logging.debug('End of program')
