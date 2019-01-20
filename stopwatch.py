#!/usr/bin/env python
import logging, time

#! python3
# stopwatch.py - A simple stopwatch program.

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')

logging.debug('Start of program')

def lap():
    


    # Display the program's instructions.
    print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
    input()                    # press Enter to begin
    print('Started.')
    startTime = time.time()    # get the first lap's start time
    lastTime = startTime
    lapNum = 1
    
    
    # TODO: Start tracking the lap times.
    
    try:
        while True:
            input()
            lapTime = round(time.time() - lastTime, 2)
            totalTime = round(time.time() - startTime, 2)
            print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
            lapNum += 1
            lastTime = time.time() # reset the last lap time
    except KeyboardInterrupt:
        # Handle the Ctrl-C exception to keep its error message from displaying.
        print('\nDone.')


def main():
    lap()
    logging.debug('End of program')

if __name__ == '__main__':
    main()
