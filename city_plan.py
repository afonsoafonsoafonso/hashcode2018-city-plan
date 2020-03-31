import sys
import time
from city import City
from building_proj import BuildingProj
from building import Building
from state import State
from utils import * 
from algorithms import *

if len(sys.argv) != 2:
    print('Wrong number of parameters.\n\nUsage: python3 city_plan.py inputFile')
    sys.exit(0)

print('Initializing...')

file_name = sys.argv[1]
city, building_projs = parseFile(file_name)
empty_map = [['.' for col in range(city.cols)] for row in range(city.rows)]
empty_state = State(city, [], empty_map, 0)

user_input = None
init_sol = getRandomSolution(empty_state, city, building_projs, empty_map)

print('Initial solution score: ' + str(init_sol.score))

while True:
    queue = []
    user_input = None
    while user_input != '0':
        print('\nCity Plan : IART 2019/2020 Project')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('Choose the algorithms you want to use to solve the problem:\n')
        print('1: Hill Climbing')
        print('2: Steepest Ascent')
        print('3: Simulated Annealing')
        print('4: Tabu Search')
        print('5: Tabu Search w/ Annealing')
        print('6: Genetic Algorithm')
        print('7: Swarm')
        print('\nAlgorithms in queue: ', end='')
        print(queue)
        print('\nInput \'0\' to solve.\n')
        user_input = input('Your option: ')
        
        if user_input == '1':
            print('~~~~~~Hill Climbing Options~~~~~~\n')
            option = input('Iterations: ')
            queue.append((hillClimbing,[int(option)]))

        elif user_input == '2':
            print('~~~~~Steepest Ascent Options~~~~~\n')
            option = input('Iterations: ')
            queue.append((steepestAscent, [int(option)]))

        elif user_input == '3':
            print('~~~Simulated Annealing Options~~~\n')
            option = input('Cooling factor: ')
            queue.append((simulatedAnnealing, [float(option)]))

        elif user_input == '4':
            print('~~~~~~Tabu Search Options~~~~~~\n')
            option1 = input('Tabu list size: ')
            option2 = input('Iterations: ')
            queue.append((tabuSearch, [int(option1), int(option2)]))
        
        elif user_input == '5':
            print('~Tabu Search w/Annealing Options~\n')
            option1 = input('Tabu list size: ')
            option2 = input('Cooling factor: ')
            queue.append((tabuSearchWithAnnealing, [int(option1), float(option2)]))

        elif user_input == '6':
            print('~~~~Genetic Algorithm Options~~~~\n')
            option1 = input('Iterations: ')
            option2 = input('Number of population per generation (multiple of 6): ')
            option3 = input('Mutation percentage: ')
            queue.append((genetic, [int(option1), int(option2), int(option3)]))

        elif user_input == '7':
            print('~~~~~~~~~~Swarm Options~~~~~~~~~~\n')
            option1 = input('Iterations: ')
            option2 = input('Distance Between Birds: ')
            queue.append((swarm, [int(option1), int(option2)]))

    print('Do you want the map to be drawn on screen for each solution?')
    print('1: Yes')
    print('2: No')
    option = int(input('Your option: '))
    if option != 1 and option != 2:
        sys.exit(1)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    i = 1
    for algorithm in queue:
        print('Algorithm #' + str(i) + ':')
        start = time.time()
        state = algorithm[0](*algorithm[1], init_sol, building_projs)
        end = time.time()
        print('Elapsed time: ' + str(end-start))
        print('Final score: ' + str(state.score))
        if option==1:
            printMap(state)
        i += 1

    print('\nDo you wish to retry with the same initial solution?')
    print('1: Yes')
    print('2: No')
    if input('Your option: ') == 2:
        break
print('\n\nFINISHED')
        