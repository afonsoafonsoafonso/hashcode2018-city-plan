import random

def d_hill_climbing(initState, city, buildingProjs, map):
    state = initState
    state = state.nextState(buildingProjs[len(buildingProjs)-1], 0, 0)

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
    state = state.nextState(buildingProjs[len(buildingProjs)-1], 0, 0)
    descendants = []

    for nrow in range(len(map)):
        for ncol in range(len(map[nrow])):
            print(str(nrow) + ',' + str(ncol))
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
    state = state.nextState(buildingProjs[len(buildingProjs)-1], 0, 0)
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