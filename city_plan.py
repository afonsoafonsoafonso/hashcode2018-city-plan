import sys
import time
from city import City
from building_proj import BuildingProj
from building import Building
from state import State
from utils import parseFile, getRandomSolution
from algorithms import *

if len(sys.argv) != 2:
    print('Wrong number of parameters.\n\nUsage: python3 city_plan.py inputFile')
    sys.exit(0)

file_name = sys.argv[1]
city, building_projs = parseFile(file_name)
empty_map = [['.' for col in range(city.cols)] for row in range(city.rows)]
empty_state = State(city, [], empty_map, 0)

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
    print('\nInput 0 to solve.\n')
    user_input = input('Your option: ')
    
    if user_input == '1':
        print('~~~~~~Hill Climbing Options~~~~~~\n')
        option = input('Iterations: ')
        queue.append((1,option))

    elif user_input == '2':
        print('~~~~~Steepest Ascent Options~~~~~\n')
        option = input('Iterations: ')
        queue.append((2,option))

    elif user_input == '3':
        print('~~~Simulated Annealing Options~~~\n')
        option = input('Cooling factor: ')
        queue.append((3,option))

    elif user_input == '4':
        print('~~~~~~Tabu Search Options~~~~~~\n')
        option1 = input('Tabu list size: ')
        option2 = input('Iterations: ')
        queue.append((4, option1, option2))
    
    elif user_input == '5':
        print('~Tabu Search w/Annealing Options~\n')
        option1 = input('Tabu list size: ')
        option2 = input('Cooling factor: ')
        queue.append((5, option1, option2))

    elif user_input == '6':
        print('~~~~Genetic Algorithm Options~~~~\n')
        option = input('Iterations: ')
        queue.append((6, option))

    elif user_input == '7':
        print('~~~~~~~~~~Swarm Options~~~~~~~~~~\n')
        option = input('Iterations: ')
        queue.append((7, option))
        