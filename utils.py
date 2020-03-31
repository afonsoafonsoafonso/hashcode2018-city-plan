import sys
import time
import random
from copy import deepcopy
from city import City
from building_proj import BuildingProj
from building import Building

def parseFile(file_name):
    buildings = []
    i = 0
    try:
        with open(file_name, 'r') as input_file:
            vars = input_file.readline().split()
            city = City(vars[0], vars[1], vars[2], vars[3])
            for line in input_file:
                plan = []
                vars = line.split()
                for nrow in range(int(vars[1])):
                    row = input_file.readline()
                    row = row.rstrip('\n')
                    plan.append(row)
                buildings.append(BuildingProj(i, vars[0], vars[1], vars[2], vars[3], plan))
                i += 1

        input_file.close()
        return city, buildings 
    except:
        print("Error opening or parsing file.")
        raise SystemExit

def getRandomSolution(init_state, city, building_projs, map):
    state = init_state
    state = state.nextState(building_projs[len(building_projs)-1], 0, 0)
    descendants = []

    for nrow in range(len(map)):
        for ncol in range(len(map[nrow])):
            print('Processing initial solution: row ' + str(nrow) + ' and column ' + str(ncol))
            descendants.clear()
            for proj in building_projs:
                new_state = state.nextState(proj, nrow, ncol)
                if new_state != False:
                    descendants.append(new_state)

            if len(descendants) > 0:
                state = random.choice(descendants)

    return state

def printMap(final_state):
    #print(final_state.score)
    for rown in range(len(final_state.map)):
        print('\n', end='')
        for coln in range(len(final_state.map[0])):
            if final_state.map[rown][coln] == '.':
                print('....|', end='')
            else:
                print(final_state.buildings[int(final_state.map[rown][coln])-1].type, end='')
                print(str(final_state.map[rown][coln]).zfill(3), end='')
                print('|', end='')
    print("\n\n")

def removeFromMap(map, building):
    new_map = deepcopy(map)
    plan = building.plan
    for prow in range(building.rows):
        for pcol in range(building.cols):
            if plan[prow][pcol] == '#':
                new_map[prow+building.mrow][pcol+building.mcol] = '.'
    return new_map
