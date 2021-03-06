#!/usr/bin/env python

import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')

logging.debug('Start of program')


class HelloWorld:

    _public_methods_ = ['Hello']

    _public_attrs_ = ['softspace', 'noCalls']

    _readonly_attrs_ = ['noCalls']

    
    def __init__(self):

        
        self.softspace = 1

        self.noCalls = 0

        

    def Hello(self, who):

        self.noCalls = self.noCalls + 1

        # insert "softspace" number of spaces

        return "Hello" + " " * self.softspace + who



def main():
    h=HelloWorld()
    logging.debug(dir(HelloWorld))

    logging.debug(h)
    h.Hello("Ray")
    logging.debug(h.Hello)
    logging.debug(h.Hello("Ray"))
    logging.debug('End of program')

if __name__ == '__main__':
    main()
