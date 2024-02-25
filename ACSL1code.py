
import math
import os
import random
import re
import sys



def findDiscardSum(originalRows, tiles):
    
    board = [str(originalRows)[0], str(originalRows)[1], str(originalRows)[2], str(originalRows)[3]]
    tiles = tiles.split(" ")
    discard = 0

    i = 0
    number = range(len(tiles))
    for r in range(50):           #find correct number of r's
        if i < len(tiles):
            tile = tiles[i]
            if r >= 4:
                for x in range(len(board)):
                    if i < len(tiles):
                        tile = tiles[i]
                        if tile[0] == board[x] or tile[1] == board[x]:  #IF THE TILE MATCHES
                            if tile[0] == board[x]:
                                board[x] = tiles[i][1]
                                break
                            elif tile[1] == board[x]:
                                board[x] = tile[0]
                                break
                if tile[0] not in board and tile[1] not in board:
                    discard += int(tile[0]) + int(tile[1])        
                                
                i = i + 1
            elif (tile[0] == board[r] or tile[1] == board[r]) and (tile[0] != tile[1]):  #IF THE TILE MATCHES
                if tile[0] == board[r]:
                    board[r] = tiles[i][1]
                    i = i + 1
                elif tile[1] == board[r]:
                    board[r] = tile[0]
                    i = i + 1
            
            if tile[0] == tile[1] and tile[0] in board:
                ogtile = tile
                c = i
                for z in range(c, len(tiles)):
                    tile = tiles[z]
                    i += 1
                    for x in range(len(board)):
                        if tile[0] == board[x] or tile[1] == board[x]:  #IF THE TILE MATCHES
                            if tile[0] == board[x]:
                                board[x] = tiles[c][1]
                                break
                            elif tile[1] == board[x]:
                                board[x] = tile[0]
                                break
                    if tile[0] not in ogtile and tile[1] not in ogtile:
                        discard += int(tile[0]) + int(tile[1]) 
                    else:
                        break
            elif tile[0] == tile[1] and tile[0] not in board and tile[1] not in board:
                discard += int(tile[0]) + int(tile[1])
                i = i + 1




    return(discard)

def main():

    originalRows = 1542

    tiles = "44 44 44 33 42 32"

    result = findDiscardSum(originalRows, tiles)
    print(result)

main()