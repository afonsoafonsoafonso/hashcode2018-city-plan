from random import randrange, uniform
from math import e
from copy import deepcopy

HC_MAX_TRIES = 5
SA_MAX_TRIES = 5

#como se escolhe o vizinho a verificar? para já está a ser escolhido um à toa
# e se for melhor está feito
def hillClimbing(init_sol, building_projs):
    state = init_sol
    tries = 0
    found_better_state = False
    while tries < HC_MAX_TRIES:
        print(tries)
        found_better_state = False
        random_building_index = randrange(0, len(state.buildings))
        random_building = state.buildings[random_building_index]
        for building_proj in building_projs:
            new_state = state.replaceBuilding(random_building_index, building_proj)
            if new_state != False and new_state.score > state.score:
                state = new_state
                found_better_state = True
                break
        if not found_better_state:
            tries += 1

    return state

def steepestAscent(init_sol, building_projs):
    state = init_sol
    tries = 0
    found_better_state = False
    while tries < SA_MAX_TRIES:
        print(tries)
        at_least_one_success = False
        random_building_index = randrange(0, len(state.buildings))
        random_building = state.buildings[random_building_index]
        for building_proj in building_projs:
            new_state = state.replaceBuilding(random_building_index, building_proj)
            if new_state != False and new_state.score > state.score:
                found_better_state = True
                tries = 0
                state = new_state
        if not found_better_state:
            tries += 1
    return state

def simulatedAnnealing(colFactor, init_sol, building_projs):
    init_t = 1000
    end_t = 1
    state = init_sol
    t = init_t
    i = 0
    while t > end_t:
        i += 1
        t *= colFactor
        random_building_index = randrange(0, len(state.buildings))
        random_building = state.buildings[random_building_index]
        for building_proj in building_projs:
            new_state = state.replaceBuilding(random_building_index, building_proj)
            if new_state != False:
                if new_state.score > state.score or t/1000 > uniform(0,1):
                    state = new_state
                    break
    print("i:" + str(i))
    return state

# critério de proíbição:
# proíbido voltar a ver possíveis vizinhos de um certo estado (aka ver
# alternativas a certo edificio) se isto já foi feito
# nas últimas tab_list_size iterações
def tabuSearch(tab_list_size, init_sol, building_projs):
    t = 1000
    end_t = 1
    col_factor = 0.995

    tabu_list = []
    state = init_sol
    while t > end_t:
        t *= col_factor
        random_building_index = randrange(0, len(state.buildings))
        random_building = state.buildings[random_building_index]
        for building_proj in building_projs:
            new_state = state.replaceBuilding(random_building_index, building_proj)
            if new_state != False and (random_building.mrow, random_building.mcol) not in tabu_list:
                if new_state.score > state.score or t/1000 > uniform(0,1):
                    if len(tabu_list) == tab_list_size:
                        tabu_list.pop(0)
                    tabu_list.append((random_building.mrow, random_building.mcol))
                    state = new_state
    return state

def genetic(init_sol, init_sol2, iter, building_projs):
    if init_sol.score > init_sol2.score:
        state = deepcopy(init_sol)
    else:
        state = deepcopy(init_sol2)
    
    parent1 = deepcopy(init_sol)
    parent2 = deepcopy(init_sol2)

    for _ in range(iter):
        parent1,parent2 = crossover(parent1, parent2, building_projs)
        parent1 = mutation(parent1, building_projs)
        parent2 = mutation(parent2, building_projs)
        
        #Saving the best descent of each iteration if they are better than the anterior
        if parent1.score > parent2.score and parent1.score > state.score:
            state = parent1
        elif parent2.score >= parent1.score and parent2.score > state.score: 
            state = parent2
    
    return state # return the overall best descendent
    
def crossover(parent1, parent2, building_projs):
    if len(parent1.buildings) <= len(parent2.buildings):
        gap = len(parent1.buildings)
    else:
        gap = len(parent2.buildings)
        
    random_first_index = randrange(0, gap-1)
    random_last_index = randrange(random_first_index, gap)
    
    descendent1 = deepcopy(parent1)
    descendent2 = deepcopy(parent2)        

    for i in range(random_first_index, random_last_index):

        newState1 = descendent1.replaceBuilding(i, building_projs[parent1.buildings[i].projId])
        newState2 = descendent2.replaceBuilding(i, building_projs[parent2.buildings[i].projId])

        if newState1 != False and newState2 != False:
            descendent1 = newState1
            descendent2 = newState2
            
    return descendent1, descendent2

def mutation(seed,building_projs):
    for x in range (len(seed.buildings)):
        r = randrange(1,101)    
        if r <= 3:
            random_building_index = randrange(0, len(building_projs))
            random_building = building_projs[random_building_index]
            new_seed = seed.replaceBuilding(x, random_building)
            if new_seed != False:
                seed = new_seed
    return seed