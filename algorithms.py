import sys
import time
from city import City
from building_proj import BuildingProj
from building import Building
from utils import *

#como se escolhe o vizinho a verificar? para já está a ser escolhido um à toa
# e se for melhor está feito
def hill_climbing(initState, city, buildingProjs, map):
    state = get_random_solution(initState, city, buildingProjs, map)
    random_building = random.choice(state.buildings)
    for building in buildingProjs:
        newMap = remove_from_map(state.map, random_building)

######## DEPRECATED #########

def d_hill_climbing(initState, city, buildingProjs, map):
    state = initState
    state = state.nextState(buildingProjs[-1], 0, 0)

    for nrow in range(len(map)):
        for ncol in range(len(map[nrow])):
            print(str(nrow) + ',' + str(ncol))
            for proj in buildingProjs:
                newState = state.nextState(proj, nrow, ncol)
                if newState != False and newState.score > state.score:
                    state = newState
                    ncol += proj.cols
                    break

    return state

def d_steepest_ascent(initState, city, buildingProjs, map):
    state = initState
    state = state.nextState(buildingProjs[-1], 0, 0)
    descendants = []

    for nrow in range(len(map)):
        for ncol in range(len(map[nrow])):
            #print(str(nrow) + ',' + str(ncol))
            descendants.clear()
            for proj in buildingProjs:
                newState = state.nextState(proj, nrow, ncol)
                if newState != False and newState.score > state.score:
                    descendants.append(newState)
            descendants.sort(key = lambda x: x.score, reverse=True)
            if len(descendants) > 0:
                state = descendants[0]

    return state

def d_hill_climbing_random(initState, city, buildingProjs, map):
    state = initState
    state = state.nextState(buildingProjs[-1], 0, 0)
    descendants = []

    for nrow in range(len(map)):
        for ncol in range(len(map[nrow])):
            print(str(nrow) + ',' + str(ncol))
            descendants.clear()
            for proj in buildingProjs:
                newState = state.nextState(proj, nrow, ncol)
                if newState != False:
                    descendants.append(newState)

            if len(descendants) > 0:
                state = random.choice(descendants)

    return state