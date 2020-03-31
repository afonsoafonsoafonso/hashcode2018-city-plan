from random import randrange, uniform
from math import e, sqrt
from copy import deepcopy
from state import State
from utils import *
import logging

def hillClimbing(max_its, init_sol, building_projs):
    #f = open("log.txt", "w")
    state = init_sol
    its = 0
    while its < max_its:
        its += 1
        #print(str(its) + ',' + str(state.score), file=f)
        random_building_index = randrange(0, len(state.buildings))
        random_building = state.buildings[random_building_index]
        for building_proj in building_projs:
            new_state = state.replaceBuilding(random_building_index, building_proj)
            if new_state != False and new_state.score > state.score:
                state = new_state
                found_better_state = True
                break
    #f.close()
    return state

def steepestAscent(max_its, init_sol, building_projs):
    #f = open("log.txt", "w")
    state = init_sol
    its = 0
    at_least_one_success = False
    while its < max_its:
        its += 1
        #print(str(its) + ',' + str(state.score), file=f)
        random_building_index = randrange(0, len(state.buildings))
        random_building = state.buildings[random_building_index]
        for building_proj in building_projs:
            new_state = state.replaceBuilding(random_building_index, building_proj)
            if new_state != False and new_state.score > state.score:
                state = new_state
    #f.close()
    return state

def simulatedAnnealing(colFactor, init_sol, building_projs):
    init_t = 1000
    end_t = 1
    state = init_sol
    t = init_t
    i = 0
    #f = open("log.txt", "w")
    while t > end_t:
        i += 1
        #print(str(i) + ',' + str(state.score), file=f)
        t *= colFactor
        random_building_index = randrange(0, len(state.buildings))
        random_building = state.buildings[random_building_index]
        for building_proj in building_projs:
            new_state = state.replaceBuilding(random_building_index, building_proj)
            if new_state != False:
                if new_state.score > state.score or t/1000 > uniform(0,1):
                    state = new_state
                    break
    print('Iterations: ' + str(i))
    #f.close()
    return state

def tabuSearch(tab_list_size, max_its, init_sol, building_projs):
    tabu_list = []
    state = init_sol
    it = 0
    while it < max_its:
        it += 1
        random_building_index = randrange(0, len(state.buildings))
        random_building = state.buildings[random_building_index]
        for building_proj in building_projs:
            new_state = state.replaceBuilding(random_building_index, building_proj)
            if new_state != False and (random_building.mrow, random_building.mcol) not in tabu_list:
                if new_state.score > state.score:
                    if len(tabu_list) == tab_list_size:
                        tabu_list.pop(0)
                    tabu_list.append((random_building.mrow, random_building.mcol))
                    state = new_state
    return state

# critério de proíbição:
# proíbido voltar a ver possíveis vizinhos de um certo estado (aka ver
# alternativas a certo edificio) se isto já foi feito
# nas últimas tab_list_size iterações
def tabuSearchWithAnnealing(tab_list_size, col_factor, init_sol, building_projs):
    t = 1000
    end_t = 1

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
def genetic(sols, iter, building_projs, population):
    f = open("log.txt", "w")
    #print("Started Genetic Algorithms!!")

    state = sols[0]
    parent1 = sols[0]
    parent2 = sols[1]
    parent3 = sols[2]

    print("tou tolo")

    """
    print("Processing first parents...")
    init_map = [['.' for col in range(sol.city.cols)] for row in range(sol.city.rows)]
    empty_state = State(sol.city, [], init_map, 0)
    parent2 = getRandomSolution(empty_state, sol.city, building_projs, init_map)
    parent3 = getRandomSolution(empty_state, sol.city, building_projs, init_map)
    print("First parents processed!!")
    """
    if parent1.score < parent2.score:
        state = parent2
    elif parent1.score < parent3.score:
        state = parent3
    #print("Best initial score: " + str(state.score))

    iterCross = population // 6

    for x in range(iter):
        #crossover
        child1 = crossover(parent1, parent2, building_projs, iterCross)
        child2 = crossover(parent2, parent3, building_projs, iterCross)
        child3 = crossover(parent1, parent3, building_projs, iterCross)
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
        parent1 = child1
        parent2 = child2
        parent3 = child3

        #logging
        print(str(x +1 ) + ',' + str(state.score), file=f)

    return state #return the overall best descendent
    
def crossover(parent1, parent2, building_projs, iterCross):
    bestChild = State(parent1.city, [], [], 0)

    if len(parent1.buildings) <= len(parent2.buildings):
        gap = len(parent1.buildings)
    else:
        gap = len(parent2.buildings)

    for i in range(iterCross):
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
def swarm(iter, distBtBirds, sol, building_projs):
    print("Started Particle Swarm Optimization!!")

    swarmSol = deepcopy(sol)
    print("Initial Score: " + str(swarmSol.score))

    #direção inicial random do lider
    hypotheses = [-1,0,1]
    while True:
        randomDeltaX = randrange(0,3)
        randomDeltaY = randrange(0,3)
        if randomDeltaX != 0 or randomDeltaY != 0:
            break

    #inicializacao dos elementos do swarm
    bird0 = Bird(sol.city.cols//2, sol.city.rows//2, hypotheses[randomDeltaX], hypotheses[randomDeltaY], True, distBtBirds, 1)
    bird1 = Bird(sol.city.cols-1, 0, 0, 0, False, distBtBirds, 1)
    bird2 = Bird(0, sol.city.rows-1, 0, 0, False, distBtBirds, 1)

    #alphaPos e alphaVel
    alphaPos = bird0.pos
    alphaVel = 1
    counter = 0
    auxDiagonal = 3 * sqrt(sol.city.cols *  sol.city.cols + sol.city.rows * sol.city.rows) // 4
    
    """
    print("bird0(x,y): (" + str(bird0.pos[0]) + "," + str(bird0.pos[1]) + ")")
    print(bird0.deltaX, bird0.deltaY, bird0.vel)
    print("bird1(x,y): (" + str(bird1.pos[0]) + "," + str(bird1.pos[1]) + ")")
    print(bird1.deltaX, bird1.deltaY, bird1.vel)
    print("bird2(x,y): (" + str(bird2.pos[0]) + "," + str(bird2.pos[1]) + ")")
    print(bird2.deltaX, bird2.deltaY, bird2.vel)
    print("################")
    """

    #loop principal
    for _ in range(iter):
        #lista de posicões para verificar que nao há colisoes
        #movimentacao dos elementos do swarm
        positions = []
        positions.append(bird1.pos)
        positions.append(bird2.pos)
        swarmSol, bird0Score = bird0.nextStep(positions, alphaPos, alphaVel, swarmSol, building_projs)
        #print("bird0(x,y): (" + str(bird0.pos[0]) + "," + str(bird0.pos[1]) + ")")
        #print(bird0.deltaX, bird0.deltaY, bird0.vel, bird0Score, str(bird0.alphaStatus))

        positions = []
        positions.append(bird0.pos)
        positions.append(bird2.pos)
        swarmSol, bird1Score = bird1.nextStep(positions, alphaPos, alphaVel, swarmSol, building_projs)
        #print("bird1(x,y): (" + str(bird1.pos[0]) + "," + str(bird1.pos[1]) + ")")
        #print(bird1.deltaX, bird1.deltaY, bird1.vel, bird1Score, str(bird1.alphaStatus))

        positions = []
        positions.append(bird0.pos)
        positions.append(bird1.pos)
        swarmSol, bird2Score = bird2.nextStep(positions, alphaPos, alphaVel, swarmSol, building_projs)
        #print("bird2(x,y): (" + str(bird2.pos[0]) + "," + str(bird2.pos[1]) + ")")
        #print(bird2.deltaX, bird2.deltaY, bird2.vel, bird2Score, str(bird2.alphaStatus))
        #print("################")

        #verificacao do melhoramento do score de cada um e estabelecimento do lider
        if bird0Score > bird1Score and bird0Score > bird2Score:
            print("+Bird0 had the best score increase!")

            alphaPos = bird0.pos

            if bird0.alphaStatus == True:
                bird0.vel += 1
            else:
                bird0.vel = 1

            alphaVel = bird0.vel
            bird0.alphaStatus = True

            bird1.alphaStatus = False
            bird1.vel = alphaVel

            bird2.alphaStatus = False
            bird2.vel = alphaVel
        elif bird1Score > bird0Score and bird1Score > bird2Score:
            print("+Bird1 had the best score increase!")

            alphaPos = bird1.pos

            if bird1.alphaStatus == True:
                bird1.vel += 1
            else:
                bird1.vel = 1

            alphaVel = bird1.vel
            bird1.alphaStatus = True

            bird0.alphaStatus = False
            bird0.vel = alphaVel

            bird2.alphaStatus = False
            bird2.vel = alphaVel
        elif bird2Score > bird0Score and bird2Score > bird1Score:
            print("+Bird2 had the best score increase!")

            alphaPos = bird2.pos

            if bird2.alphaStatus == True:
                bird2.vel += 1
            else:
                bird2.vel = 1

            alphaVel = bird2.vel
            bird2.alphaStatus = True

            bird0.alphaStatus = False
            bird0.vel = alphaVel

            bird1.alphaStatus = False
            bird1.vel = alphaVel
        else:
            counter += 1
            if bird0.alphaStatus == True:
                if counter > auxDiagonal:
                    randX = randrange(0, sol.city.cols)
                    randY = randrange(0, sol.city.rows)
                    bird0.pos = (randX, randY)
                alphaPos = bird0.pos
            elif bird1.alphaStatus == True:
                if counter > auxDiagonal:
                    randX = randrange(0, sol.city.cols)
                    randY = randrange(0, sol.city.rows)
                    bird1.pos = (randX, randY)
                alphaPos = bird1.pos
            else:
                if counter > auxDiagonal:
                    randX = randrange(0, sol.city.cols)
                    randY = randrange(0, sol.city.rows)
                    bird2.pos = (randX, randY)
                alphaPos = bird2.pos
                
            alphaVel = 1
            bird0.vel = alphaVel
            bird1.vel = alphaVel
            bird2.vel = alphaVel

        bird0Score = 0
        bird1Score = 0
        bird2Score = 0
    
    return swarmSol


class Bird:
    def __init__(self, x, y, deltaX, deltaY, alphaStatus, distBtBirds, vel):
        self.pos = (x,y)
        self.deltaX = deltaX
        self.deltaY = deltaY
        self.alphaStatus = alphaStatus
        self.distBtBirds = distBtBirds
        self.vel = vel
    
    def nextStep(self, positions, alphaPos, alphaVel, swarmSol, building_projs):#positions(dos outros birds); alphaVel(velocidade do líder(1,2,3..))
        if abs(self.deltaX) == 0.0 and abs(self.deltaY) == 0.0:
            #print("aiiii")
            hypotheses = [-1,0,1]
            while True:
                randomDeltaX = randrange(0,3)
                randomDeltaY = randrange(0,3)
                if randomDeltaX != 0 or randomDeltaY != 0:
                    break
            self.deltaX = hypotheses[randomDeltaX]
            self.deltaY = hypotheses[randomDeltaY]
            self.pos = (self.pos[0] + self.deltaX * self.vel, self.pos[1] + self.deltaY * self.vel)
            self.verifyPos(swarmSol)
        elif self.alphaStatus == True:
            self.pos = (self.pos[0] + self.deltaX * self.vel, self.pos[1] + self.deltaY * self.vel)
            self.verifyPos(swarmSol)
        else:
            #print("se fodeu")
            distX = alphaPos[0] - self.pos[0]
            distY = alphaPos[1] - self.pos[1]
            norma = sqrt(distX * distX + distY * distY)
            if norma != 0:
                self.deltaX = distX // norma
                self.deltaY = distY // norma
            else:
                self.deltaX = - self.deltaX
                self.deltaY = - self.deltaY
            #print(self.deltaX, self.deltaY, self.pos, self.vel)
            self.pos = (self.pos[0] + self.deltaX * self.vel, self.pos[1] + self.deltaY * self.vel)
            self.verifyPos(swarmSol)
            #print(self.deltaX, self.deltaY, self.pos, self.vel)

        for i in range(len(positions)):
            if calcManhattanDist(self.pos[0], self.pos[1], positions[i][0], positions[i][1]) <= self.distBtBirds:
                #print("tou tolo")
                self.deltaX = - self.deltaX
                self.deltaY = - self.deltaY
                self.pos = (self.pos[0] + self.deltaX * self.vel, self.pos[1] + self.deltaY * self.vel)
                distX = alphaPos[0] - self.pos[0]
                distY = alphaPos[1] - self.pos[1]
                norma = sqrt(distX * distX + distY * distY)
                if norma != 0:
                    auxDeltaX = distX // norma
                    auxDeltaY = distY // norma
                    if randrange(0,2) == 0:
                        self.deltaX = - auxDeltaY
                        self.deltaY = auxDeltaX
                    else:
                        self.deltaX = auxDeltaY
                        self.deltaY = - auxDeltaX
                self.pos = (self.pos[0] + self.deltaX * self.vel, self.pos[1] + self.deltaY * self.vel)
                self.verifyPos(swarmSol)
                break

        if self.pos[0] < 0 or self.pos[0] > (swarmSol.city.cols - 1) or self.pos[1] < 0 or self.pos[1] > (swarmSol.city.rows -1):
            randX = randrange(0, swarmSol.city.cols)
            randY = randrange(0, swarmSol.city.rows)
            self.pos = (randX, randY)
    
        prevScore = swarmSol.score
        newSol = self.optimizePosition(self.pos, swarmSol, building_projs)

        return newSol, newSol.score - prevScore

    def verifyPos(self, swarmSol):
        if self.pos[0] < 0 or self.pos[0] > (swarmSol.city.cols - 1) or self.pos[1] < 0 or self.pos[1] > (swarmSol.city.rows -1):
            self.deltaX = - self.deltaX
            self.deltaY = - self.deltaY
            self.pos = (self.pos[0] + 2 * self.deltaX * self.vel, self.pos[1] + 2 * self.deltaY * self.vel)

    
    def optimizePosition(self, position, swarmSol, building_projs):
        prevState = swarmSol
        bestState = swarmSol
        x = int(position[0])
        y = int(position[1])
        buildingIndex = prevState.map[y][x]

        for proj in building_projs:
            if buildingIndex == '.':
                newState = prevState.nextState(proj, y, x)
            else:
                newState = prevState.replaceBuilding(buildingIndex - 1, proj)            

            if newState != False and newState.score > bestState.score:
                #print("mais score pah")
                bestState = newState

        return bestState
            
def calcManhattanDist(row1, col1, row2, col2):
    return (abs(row2 - row1) + abs(col2 - col1))
