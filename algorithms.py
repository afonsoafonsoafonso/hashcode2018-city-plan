from random import randrange, uniform
from math import e
from utils import get_random_solution

#como se escolhe o vizinho a verificar? para já está a ser escolhido um à toa
# e se for melhor está feito
def hill_climbing(initSol, buildingProjs):
    state = initSol
    for it in range(0,1379):
        random_building_index = randrange(0, len(state.buildings))
        random_building = state.buildings[random_building_index]
        for buildingProj in buildingProjs:
            newState = state.replace_building(random_building_index, buildingProj)
            if newState != False and newState.score > state.score:
                state = newState
                break

    return state

def steepest_ascent(initSol, buildingProjs):
    state = initSol
    for it in range(0,1379):
        random_building_index = randrange(0, len(state.buildings))
        random_building = state.buildings[random_building_index]
        for buildingProj in buildingProjs:
            newState = state.replace_building(random_building_index, buildingProj)
            if newState != False and newState.score > state.score:
                state = newState

    return state

def simulated_annealing(colFactor, initSol, buildingProjs):
    initT = 1000
    endT = 1
    state = initSol
    T = initT
    i = 0
    while T > endT:
        i += 1
        T *= colFactor
        random_building_index = randrange(0, len(state.buildings))
        random_building = state.buildings[random_building_index]
        for buildingProj in buildingProjs:
            newState = state.replace_building(random_building_index, buildingProj)
            if newState != False:
                diff = newState.score - state.score
                if diff > 0 or T/1000 > uniform(0,1):
                    state = newState
                    break
    print("i:" + str(i))
    return state
        

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