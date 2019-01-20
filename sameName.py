#!/usr/bin/env python

def spam():
    eggs='spam local'
    print(eggs) #prints 'spam local

def bacon():
    eggs='bacon local'
    print(eggs) #prints 'bacon local
    spam()
    print(eggs) #prints 'bacon local'
    


def main():
    eggs='global'
    bacon()
    print(eggs) #prints global
     

if __name__ == '__main__':
    main()
