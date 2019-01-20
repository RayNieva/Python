#!/usr/bin/env python

import logging, pythoncom
from win32com.server.exception import COMException
import win32com.server.util
import win32com.client.dynamic

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')

logging.debug('Start of program')


class HelloWorld:

    _reg_clsid_ = "{4201D782-31A9-4933-958F-1C10617A2A2F}"

    assert _reg_clsid_ !=None

    _reg_desc_ = "Python Test COM Server"

    _reg_progid_ = "Python.TestServer"

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
    logging.debug(h)
    logging.debug(dir(h))
    h.Hello("Ray")
    logging.debug(h.Hello)
    logging.debug(h.Hello("Ray"))
    

if __name__ == '__main__':
    main()

    import win32com.server.register
    
    win32com.server.register.UseCommandLine(HelloWorld)
    logging.debug('End of program')

