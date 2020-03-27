from random import randrange, uniform
from math import e, sqrt
from copy import deepcopy
from state import State

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

############# GENETIC ALGORITHM #############
def genetic(sols, iter, building_projs, populationDiv6): #populationDiv6 corresponde ao valor da (população de cada geração)/6, no caso de populationDiv6=5, população=30
    state = sols[0]
    for i in range(1,len(sols)):
        if sols[i].score > state.score:
            score = deepcopy(sols[i])
    
    parent1 = deepcopy(sols[0])
    parent2 = deepcopy(sols[1])
    parent3 = deepcopy(sols[2])

    for _ in range(iter):
        #crossover
        child1 = crossover(parent1, parent2, building_projs, populationDiv6)
        child2 = crossover(parent2, parent3, building_projs, populationDiv6)
        child3 = crossover(parent1, parent3, building_projs, populationDiv6)
        #mutation
        child1 = mutation(child1, building_projs)
        child2 = mutation(child2, building_projs)
        child3 = mutation(child3, building_projs)
        
        #Saving the best descent of each iteration if they are better than the anterior
        if child1.score >= child2.score and child1.score >= child3.score and child1.score >= state.score:
            state = child1
        elif child2.score > child1.score and child2.score > child3.score and child2.score > state.score:
            state = child2
        elif child3.score > child1.score and child3.score > child2.score and child3.score > state.score:
            state = child3

        #childs become parents in the next iteration
        parent1=child1
        parent2=child2
        parent3=child3

    return state #return the overall best descendent
    
def crossover(parent1, parent2, building_projs, populationDiv6):
    bestChild = State(parent1.city, [], [], 0)

    if len(parent1.buildings) <= len(parent2.buildings):
        gap = len(parent1.buildings)
    else:
        gap = len(parent2.buildings)

    for i in range(populationDiv6):
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
    
        if descendent1.score >= descendent2.score and descendent1.score > bestChild.score:
            bestChild = descendent1
        elif descendent2.score > descendent1.score and descendent2.score > bestChild.score:
            bestChild = descendent2

    return bestChild

def mutation(seed,building_projs):
    for x in range (len(seed.buildings)):
        r = randrange(1,101)    
        if r <= 30:
            random_building_index = randrange(0, len(building_projs))
            random_building = building_projs[random_building_index]
            new_seed = seed.replaceBuilding(x, random_building)
            if new_seed != False:
                seed = new_seed
    return seed

############# PARTICLE SWARM OPTIMIZATION #############
def swarm(sol, iter, building_projs):
    swarmSol = deepcopy(sol)

    hypotheses = [-1,0,1]
    randomDeltaX = randrange(0,3)
    randomDeltaY = randrange(0,3)

    bird0 = Bird(sol.city.cols//2, sol.city.rows//2, hypotheses[randomDeltaX], hypotheses[randomDeltaY], True, sol.city.walk_dist)
    bird1 = Bird(sol.city.cols-1, sol.city.rows//2, 0, 0, False, sol.city.walk_dist)
    bird2 = Bird(sol.city.cols//2, sol.city.rows-1, 0, 0, False, sol.city.walk_dist)

    for _ in range(iter):
        bird0.nextStep
        bird1.nextStep
        bird2.nextStep
    
    return swarmSol


class Bird:
    def __init__(self, x, y, deltaX, deltaY, alphaStatus, distBtBirds):
        self.x = x
        self.y = y
        self.deltaX = deltaX
        self.deltaY = deltaY
        self.alphaStatus = alphaStatus
        self.distBtBirds = distBtBirds
    
    def nextStep(self, positions, alphaPos, alphaVel):#positions(dos outros birds); alphaVel(velocidade do líder(1,2,3..))
        if self.alphaStatus == True:
            self.x += self.deltaX
            self.y += self.deltaY
        else:
            self.deltaX = (self.x - alphaPos[0]) // sqrt(alphaPos[0] * alphaPos[0] + alphaPos[1] * alphaPos[1])
            self.deltaY = (self.y - alphaPos[1]) // sqrt(alphaPos[0] * alphaPos[0] + alphaPos[1] * alphaPos[1])

            self.x += self.deltaX
            self.y += self.deltaY

        for i in range(len(positions)):
            if calcManhattanDist(self.x, self.y, positions[i][0], positions[i][1]) <= self.distBtBirds:
                self.deltaX = (self.x - positions[i][0]) // sqrt(positions[i][0] * positions[i][0] + positions[i][1] * positions[i][1])
                self.deltaY = (self.y - positions[i][1]) // sqrt(positions[i][0] * positions[i][0] + positions[i][1] * positions[i][1])

                self.x -= self.deltaX
                self.y -= self.deltaY
                break
            
def calcManhattanDist(row1, col1, row2, col2):
    return (abs(row2 - row1) + abs(col2 - col1))
