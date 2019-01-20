#!/usr/bin/env python

def spam():
    global eggs
    eggs='spam'


eggs='global'
spam()
print(eggs)
    
"""    
def main():
    eggs='global'
    spam()
    print(eggs)

if __name__ == '__main__':
    main()
"""
# Interesting when I change from outside a function this code works!
