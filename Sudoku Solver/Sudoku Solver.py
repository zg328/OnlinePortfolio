# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 19:07:23 2021
different methods to clean up my puzzle code
and try some different things out
@author: zach
"""
class stuff:
    def __init__(self,board):
        self.board = board
    
    """
    def fill_puzzle(self):
        boxes = self.make_boxes()
        puzzle_boxes = {}
        for k in range(9):
            puzzle_boxes[k+1] = stuff(boxes[k+1])
            l = puzzle_boxes[k+1].check_numbers()
            for i,row in enumerate(puzzle_boxes[k+1]):
                for j,col in enumerate(puzzle_boxes[k+1]):
                    if puzzle_boxes[k][i][j] not in l:
                        puzzle_boxes[k][i][j] = l[0]
                        l.pop(0)
    """
    def check_puzzle_numbers(self):
        p = self.board
        p = stuff(p)
        pnums = {1:9,2:9,3:9,4:9,5:9,6:9,7:9,8:9,9:9}
        b = p.make_boxes()
        for i in range(9):
            
            for k,row in enumerate(b[i+1]):
                for j,col in enumerate(b[i+1]):
                    if b[i+1][k][j] >= 1 or b[i+1][k][j] <= 9:
                        pnums[b[i+1][k][j]] -= 1
        return(pnums)
    
    def check_box_numbers(self):
        box = self.board
        l = [1,2,3,4,5,6,7,8,9]
        for i,row in enumerate(box):
            for j,col in enumerate(box):
                if box[i][j] in l:
                    l.remove(box[i][j])
        return(l)
    def make_boxes(self):
        p = self.board
        boxes = {}
        bc = 1
        y = 0
        while y < 3:
            if y == 0:
                x = 1
                while x <= 3:
                    cb = []
                    for i in range(3):
                        ccol = []
                        for j in range(3):
                            ccol.append(p[i][j])
                        cb.append(ccol)
                        boxes[bc] = cb
                        bc += 1
                        x+=1
                y = y + 1
            if y == 1:
                x = 1
                while x <= 3:
                    cb = []
                    for i in range(3):
                        ccol = []
                        for j in range(3):
                            ccol.append(p[i+3][j*x])
                        cb.append(ccol)
                        boxes[bc] = cb
                        bc += 1
                        x+=1
                y = y + 1
            if y == 2:
                x = 1
                while x <= 3:
                    cb = []
                    for i in range(3):
                        ccol = []
                        for j in range(3):
                            ccol.append(p[i+6][j*x])
                        cb.append(ccol)
                        boxes[bc] = cb
                        bc += 1
                        x+=1
                y = y + 1
        return(boxes)
                    
                        
                    
        
        