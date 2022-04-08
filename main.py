# -*- coding: utf-8 -*-
"""
Tower of Hanoi - A stack moving puzzle game
"""
 
from tower import *   
   
def main():
    
    print("Move the tower of disks, one disk at a time, to another tower. Larger disks cannot rest on top of a smaller disk")
    disks_n = int(input(f"Enter no. of disks (< {TOTAL_DISKS}): "))
    if disks_n > TOTAL_DISKS or disks_n <=0:
        # set number of disks to max total disks if user entered invalid number
        print(f"Invalid number. Setting to {TOTAL_DISKS}")
        disks_n = TOTAL_DISKS
    
    # Tower A's disks to be transferred to Tower C
    a = Tower(disks_n, 'A')
    b = Tower(0, 'B')
    c = Tower(0, 'C')
    
    disks_to_move = len(a.disks)
    
    n = 0 # no. of moves
    
    # Take a single move in each iteration
    while True:
        
        # display towers
        a.display()
        b.display()
        c.display()
        
        if disks_to_move == len(c.disks):
            # Puzzle solved
            print(f"You solved the puzzle in {n} moves")
            break
        
        # Game instructions
        print("Enter the letters of \"from\" and \"to\" towers, or Q to QUIT.")
        print("(e.g. AB to move a disk from tower A to tower B.)")
        
        # Take input move
        move = input(" > ").strip().upper()
        if move == 'Q': 
            break # quit
        # Check if move is valid
        elif len(move) == 2 and move[0] in ['A','B', 'C'] and move[1] in ['A','B', 'C']:
            from_tower = [tower for tower in [a,b,c] if tower.id == move[0]][0]
            to_tower = [tower for tower in [a,b,c] if tower.id == move[1]][0]
            
            if not to_tower.add_disk(from_tower.remove_disk()):
                # if adding disk fails, put the disk back in from_tower
                from_tower.add_disk(len(from_tower.disks) + 1) 
            
            else:
                # move made
                n += 1
            
        else:
            print("Invalid move")
                    
        
    
if __name__ == "__main__":
    main()
    
    

