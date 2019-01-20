#!/usr/bin/env python
import logging, threading, time

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')

logging.debug('Start of program')

def threadDemo():
    


    print('Start of program.')
    
    def takeANap():
        time.sleep(5)
        print('Wake up!')
    
    threadObj = threading.Thread(target=takeANap)
    threadObj.start()
    
    print('End of program.')




def main():
    threadDemo()
    logging.debug('End of program')

if __name__ == '__main__':
    main()
