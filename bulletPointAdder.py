#!/usr/bin/env python

# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.
#import pyperclip 


def main():
   import pyperclip
   text=pyperclip.paste() 

   # TODO: Separate lines and add starts.
   
   lines=text.split('\n')
   print(lines)
   for i in range(len(lines)):   #loop thru all indexes in the "lines" list
       lines[i]='* ' + lines[i]  #add star to each string in "lines" list
       print(lines[i])
       
   text='\n'.join(lines)
   pyperclip.copy(text)


if __name__ == '__main__':
    main()
