#!/usr/bin/env python

def main():
    def eggs(someParameter):
        someParameter.append('Hello')

    spam=[1,2,4]
    #print(args) this does not work since arg or someParameter has no meaning in
    ## the function as a value it is only specifying a pattern in the function
    print(spam)
    eggs(spam)
    print(spam)
        
    

if __name__ == '__main__':
    main()
