#!/usr/bin/env python

"""Project Table Printer
Write a function named printTable() that takes a list of lists of strings and displays it in a well-organized table with each column right-justified. Assume that all the inner lists will contain the same number of strings. For example, the value could look like this:"""

import pprint 


def main():
    


    tableData = [['apples', 'oranges', 'cherries', 'banana'],
                 ['Alice', 'Bob', 'Carol', 'David'],
                 ['dogs', 'cats', 'moose', 'goose']]
    
    tableData
    firstColumn=tableData[0]
    firstColumn
    secondColumn=tableData[1]
    secondColumn
    thirdColumn=tableData[2]
    thirdColumn
    thirdColumn[0]
    
    len(firstColumn[0])
    
    numOfColumnWidths1=len(firstColumn)
    numOfColumnWidths2=len(secondColumn)
    numOfColumnWidths3=len(thirdColumn)
    
    
    columnWidths1=[]
    columnWidths2=[]
    columnWidths3=[]
    
    
    
    #columnWidths.append(n)
    
    
    for i in range(numOfColumnWidths1):
        print(len(firstColumn[i]))
        n=len(firstColumn[i])
        columnWidths1.append(n)    
    
    print(columnWidths1)
    
    
    columnWidths1.sort(reverse=True)
    
    columnWidths1[0]
    
    for i in range(numOfColumnWidths2):
        print(len(secondColumn[i]))
        n=len(secondColumn[i])
        columnWidths2.append(n)    
    
    print(columnWidths2)
    
    
    columnWidths2.sort(reverse=True)
    
    print(columnWidths2[0])
    
    for i in range(numOfColumnWidths3):
        print(len(thirdColumn[i]))
        n=len(thirdColumn[i])
        columnWidths3.append(n)    
    
    print(columnWidths3)
    
    
    columnWidths3.sort(reverse=True)
    
    print(columnWidths3[0])
    
    
    
    
    
    # 'A String'.rjust(columnWidths[0] + 2)
    
    """
    for i in range(numOfColumnWidths):
           print(firstColumn[i],secondColumn[i],thirdColumn[i])
    """
    
    for i in range(numOfColumnWidths1):
           print(firstColumn[i].rjust(columnWidths1[0] + 2),secondColumn[i].rjust(columnWidths2[0] + 2),thirdColumn[i].rjust(columnWidths3[0] + 2))



if __name__ == '__main__':
    main()
