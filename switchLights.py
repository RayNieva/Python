#!/usr/bin/env python
import logging 


logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

logging.debug('Start of program')


market_2nd = {'ns': 'green', 'ew': 'red'}
logging.debug('market_2nd= '+ str(market_2nd))

mission_16th = {'ns': 'red', 'ew': 'green'}
logging.debug('mission_2nd= '+ str(mission_16th))


def switchLights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'

        assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight)



def main():
    logging.debug('Entering Main')
    #switchLights(market_2nd)
    switchLights(mission_16th)
    


if __name__ == '__main__':
    main()
    logging.debug('End of program')
