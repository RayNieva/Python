#!/usr/bin/env python

def spam(divideBy):
    try:
         return 42/divideBy
   
    except ZeroDivisionError:
        print('Error: Invalid argument.')
        
        
#print(spam(2))
#print(spam(12))
#print(spam(0))
#print(spam(1))




def main():
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))


    
if __name__ == '__main__':
    main()

