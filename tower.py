# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 11:29:58 2022

@author: Dell 2015
"""

TOTAL_DISKS = 4

    
"""The stack of disks""" 
class Tower:
   
    def __init__(self, disks_no, id):
        self.disks = []
        self.id = id
        while disks_no:
            self.disks.append(disks_no)
            disks_no -= 1
      
    def add_disk(self,disk_no):
        last = self.disks[-1] if len(self.disks) else disk_no
        if disk_no > last:
            print("Cannot add larger disk onto a small one.")
            return False
        elif disk_no == 0:
            print("No disk to add.")
            return True
        else:
            self.disks.append(disk_no)
            return True
    
    def remove_disk(self):
        if len(self.disks): return self.disks.pop()
        return 0
    
    def display(self):
        width = TOTAL_DISKS*2 + 1
        disks = self.disks.copy()
        for _ in range(0, TOTAL_DISKS - len(disks)):
            print('||'.center(width))
        while len(disks):
            disk = disks.pop()
            line = disk*'o' + '_' + str(disk) + disk*'o'
            print(line.center(width))
            
        print(self.id.center(width) + '\n')