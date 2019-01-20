#!/usr/bin/env python

def main():
    myPets=['Zophie', 'Pooka', 'Fat-tail']
    print('Enter a pet name:')
    name=input()
    if name not in myPets:
        print('I do not have a pet named ' + name)
        
    else:
        print(name + ' is my pet.')
            



if __name__ == '__main__':
    main()
