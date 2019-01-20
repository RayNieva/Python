#!/usr/bin/env python

def main():
    allPlayers={'Player 1':{'rope':1,'torch':6},
               'Player 2':{'gold coin':42,'arrow':2},
               'Player 3':{'dagger':1,'apple pies':1}}

    def displayInventory(players, item):
        numItems=0
        for k, v in players.items():
            numItems = numItems + v.get(item,0)
        return  numItems

    
    def totalInventory():
        total=displayInventory(allPlayers, 'rope')  
        total=total + displayInventory(allPlayers, 'torch')
        total=total + displayInventory(allPlayers, 'gold coin')
        total=total + displayInventory(allPlayers, 'dagger')
        total=total + displayInventory(allPlayers, 'arrow')
        return total
        
    

    print('Inventory:')
    print(str(displayInventory(allPlayers, 'rope')) + ' - Rope         ') 
    print(str(displayInventory(allPlayers, 'torch'))+ ' - Torch        ') 
    print(str(displayInventory(allPlayers, 'gold coin')) + '- Gold Coins   ') 
    print(str(displayInventory(allPlayers, 'dagger'))+ ' - Dagger       ') 
    print(str(displayInventory(allPlayers, 'arrow'))+ '  - Arrow        ')
    print("Total Number of Items " + str(totalInventory()))

    print('')
    print('New Inventory after Dragons Loot, Note this is based on a new original inventory')


    def addToInventory(inventory, addItems):
        for k in dragonLoot:
            print(k)
            inv.setdefault(k,1)
            if inv[k]>1:
                inv[k]=inv[k]+1    
        
    


    inv = {'gold coin': 42, 'rope': 1}
    
    dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

    addToInventory(inv,dragonLoot)

    print(inv)
    
        
if __name__ == '__main__':
    main()
