#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 11:58:39 2016

@author: nicolefitzgerald
"""

class Game(object):
    
    def __init__(self, state, infiniteBoard=True):
        self.state = state
        self.width = state.width
        self.height = state.height
        self.infiniteBoard = infiniteBoard
        
    def step(self, count = 1):
        
        for generation in range(count):    
            newBoard = [[False] * self.width for row in range(self.height)]

            for y, row in enumerate(self.state.board):
                for x, cell in enumerate(row):
                    neighbours = self.neighbours(x, y)
                    previousState = self.state.board[y][x]
                    shouldLive = neighbours == 3 or(neighbours == 2 and previousState == True)
                    newBoard[y][x] = shouldLive
        
            self.state.board = newBoard
        
    
    def neighbours(self, x, y):
        
        count = 0
        
        for hor in [-1, 0, 1]:
            for ver in [-1, 0, 1]:
                if not hor == ver == 0 and (self.infiniteBoard == True or (0 <= x + hor < self.width and 0 <= y + ver < self.height)):
                    count += self.state.board[(y+ ver) % self.height][(x + hor) % self.width]
        
        return count
        
    def display(self):
        return self.state.display()

class State(object):
    
    def __init__(self, positions, x, y, width, height):
        
        activeCells = []

        for y, row in enumerate(positions.splitlines()):
            for x, cell in enumerate(row.strip()):
                if cell == 'o':
                    activeCells.append((x, y))
        
        board = [[False] * width for row in range(height)]

        for cell in activeCells:
            board[cell[1] +y][cell[0] + x] = True

        self.board = board
        self.width = width
        self.height = height
        
    
    def display(self):
        
        output = ''
        
        for y, row in enumerate(self.board):
            for x, cell in enumerate(row):
                if self.board[y][x]:
                    output += ' o'
                else:
                    output += ' .'
            output += '\n'
        
        return output
        
glider = """...
            o.o
            o.."""

myGame = Game(State(glider, x=2, y=3, width=10, height=10))

def main():
    theCount = 1
    while theCount < 20:
        print(myGame.display())
        myGame.step(theCount)
        theCount += 1

main()