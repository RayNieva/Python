#!/usr/bin/env python
def spam():
    print(eggs) #ERROR!
    eggs='spam local'

eggs ='global'
spam()
    





def main():
    pass

if __name__ == '__main__':
    main()
