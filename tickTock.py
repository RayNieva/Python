#!/usr/bin/env python

# This is tickTock.py Sort of a metronome that uses the sleep function.

import logging, time

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')

logging.debug('Start of program')


def tickTock():
    

    for i in range(3):
        print('Tick')
        time.sleep(1)
        print('Tock')
        time.sleep(1)
    time.sleep(5)
    logging.debug('And then sleeps for another 5')


def main():
    tickTock()
    logging.debug('End of program')

if __name__ == '__main__':
    main()
