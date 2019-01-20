#!/usr/bin/env python
#import pprint 



def main():
    message='It was a bright cold day in April, and the clocks were striking thirteen'
    count={}

    for character in message:
        count.setdefault(character, 0)
        count[character]=count[character]+1

    print(count)
    #pprint.pprint(count)
        
        

    
if __name__ == '__main__':
    main()
