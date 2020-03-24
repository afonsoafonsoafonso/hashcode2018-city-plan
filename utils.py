import sys
import time
import random
from copy import deepcopy
from city import City
from building_proj import BuildingProj
from building import Building
from algorithms import *

def parse_file(file_name):
    buildings = []
    i = 0
    try:
        with open(file_name, 'r') as input_file:
            vars = input_file.readline().split()
            city = City(vars[0], vars[1], vars[2], vars[3])
            for line in input_file:
                i += 1
                plan = []
                vars = line.split()
                for nrow in range(int(vars[1])):
                    row = input_file.readline()
                    row = row.rstrip('\n')
                    plan.append(row)
                buildings.append(BuildingProj(i, vars[0], vars[1], vars[2], vars[3], plan))

        input_file.close()
        return city, buildings 
    except:
        print("Error opening or parsing file.")
        raise SystemExit

def get_random_solution(initState, city, buildingProjs, map):
    state = initState
    state = state.nextState(buildingProjs[len(buildingProjs)-1], 0, 0)
    descendants = []

    for nrow in range(len(map)):
        for ncol in range(len(map[nrow])):
            #print(str(nrow) + ',' + str(ncol))
            descendants.clear()
            for proj in buildingProjs:
                newState = state.nextState(proj, nrow, ncol)
                if newState != False:
                    descendants.append(newState)

            if len(descendants) > 0:
                state = random.choice(descendants)

    return state

def print_map(finalState):
    print(finalState.score)
    for rown in range(len(finalState.map)):
        print('\n', end='')
        for coln in range(len(finalState.map[0])):
            if finalState.map[rown][coln] == '.':
                print('....|', end='')
            else:
                print(finalState.buildings[int(finalState.map[rown][coln])-1].type, end='')
                print(str(finalState.map[rown][coln]).zfill(3), end='')
                print('|', end='')

def remove_from_map(map, building):
    new_map = deepcopy(map)
    plan = building.plan
    for prow in range(building.rows):
        for pcol in range(building.cols):
            if plan[prow][pcol] == '#':
                new_map[prow+building.mrow][pcol+building.mcol] = '.'
    return new_map

######## DEPRECATED #########

def d_parse_file(file_name):
    buildings = []
    bestUs = {}
    bestRindex = None
    i = 0
    bestR = None
    
    with open(file_name, 'r') as input_file:
        vars = input_file.readline().split()
        city = City(vars[0], vars[1], vars[2], vars[3])
        for line in input_file:
            i += 1
            plan = []
            vars = line.split()
            for nrow in range(int(vars[1])):
                row = input_file.readline()
                row = row.rstrip('\n')
                plan.append(row)
                building = BuildingProj(i, vars[0], vars[1], vars[2], vars[3], plan)
                if building.type == 'R':
                    if bestR == None:
                        bestR = building
                    elif building.ratio > bestR.ratio:
                        bestR = building
                elif building.type == 'U':
                    if building.cenas not in bestUs.keys():
                        bestUs[building.cenas] = building
                    elif building.rows * building.cols < bestUs[building.cenas].rows * bestUs[building.cenas].cols:
                        bestUs[building.cenas] = building
    input_file.close()
    return city, bestR, bestUs.values()