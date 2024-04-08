def findpoints(rack):
        rack.append(0)
        rack.append(0)
        numcards = []
        sequences = []
        for i in range(len(rack)):
            numcards.append(int(rack[i]))
        for i in range(len(rack)-2):
            if int(rack[i])+2 == int(rack[i+2]):
                sequences.append(int(rack[i]))
                sequences.append(int(rack[i+1]))
                sequences.append(int(rack[i+2]))
        sequences = list(set(sequences))
        points = sum(numcards) + 5*len(sequences)
        return(points)

def playRackO():
    info = "10 60"
    rack = "20 110 30 16 84 40 91 69 75 7 81 15"
    pile = "39 47 114 55 35 71 25 123 51 23 34 10 77 36 115"

    info = info.split(" ")
    rack = rack.split(" ")
    pile = pile.split(" ")

    print(rack)
    
    if rack != sorted(rack):
        for pilecard in range(len(pile)):
            done = False
            for slot in range(len(rack)):
                if int(pile[pilecard]) == int(rack[slot]) - 1 and slot != 0:                #Rule 1
                    rack[slot-1] = pile[pilecard]
                    print(rack)
                    for z in range(len(rack)):
                        rack[z] = int(rack[z])
                    if rack == sorted(rack):
                        return(findpoints(rack))
                    else:
                        done = True
                        break
            if done == True:
                continue
            for slot in range(len(rack)):
                if int(pile[pilecard]) == int(rack[slot]) + 1 and slot != len(rack)-1:    #Rule 2
                    rack[slot+1] = pile[pilecard]
                    print(rack)
                    for z in range(len(rack)):
                        rack[z] = int(rack[z])
                    if rack == sorted(rack):
                        return(findpoints(rack))
                    else:
                        done = True
                        break
            if done == True:
                continue
            for slot in range(len(rack)):
                if slot != 0 and slot != len(rack)-1:                                     #Rule 3
                    if (int(rack[slot-1]) < int(rack[slot]) < int(rack[slot+1])) and slot != 0:
                        pass
                    elif (int(rack[slot-1]) < int(pile[pilecard]) < int(rack[slot+1])) and slot != 0:
                        rack[slot] = pile[pilecard]
                        for z in range(len(rack)):
                            rack[z] = int(rack[z])
                        print(rack)
                        if rack == sorted(rack):
                            return(findpoints(rack))
                            quit()
                        else:
                            done = True
                            break
            if done == True:
                continue
            for slot in range(len(rack)):
                if (int(pile[pilecard]) < int(rack[1])) and (int(rack[0]) > int(rack[1])):    #Rule 4
                    rack[0] = pile[pilecard]
                    print(rack)
                    for z in range(len(rack)):
                        rack[z] = int(rack[z])
                    if rack == sorted(rack):
                        return(findpoints(rack))
                    else:
                        done = True
                        break
            if done == True:
                continue
            for slot in range(len(rack)):                                                  #Rule 5
                if (int(pile[pilecard]) > int(rack[-2])) and (int(rack[-1]) < int(rack[-2])):
                    rack[-1] = pile[pilecard]
                    print(rack)
                    for z in range(len(rack)):
                        rack[z] = int(rack[z])
                    if rack == sorted(rack):
                        return(findpoints(rack))
                    else:
                        done = True
                        break
            if done == True:
                continue
    else:
        return(findpoints(rack))

    points = []
    for i in range(len(rack)-1):
        if rack[i] > rack[i+1]:
            points.append(-1)
    print(rack)
    return(sum(points))
    
print(playRackO())
