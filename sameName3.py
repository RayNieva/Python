#!/usr/bin/env python

def spam():
    global eggs
    eggs='spam' # this is the global

def bacon():
    eggs='bacon' # this is local
    
def ham():
    print(eggs) # this is the global

eggs=42 # this is the global
spam()
print(eggs)
    
"""
def main():
    pass

if __name__ == '__main__':
    main()
"""
