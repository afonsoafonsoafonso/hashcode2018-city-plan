import sys
import time
from city import City
from building_proj import BuildingProj
from building import Building
from state import State
from utils import *
from algorithms import *

#USAGE: python3 main.py input_file
    
file_name = sys.argv[1]
city, buildingProjs = parse_file(file_name)
initMap = [['.' for col in range(city.cols)] for row in range(city.rows)]
emptyState = State(city, [], initMap, 0)
initSol = get_random_solution(emptyState, city, buildingProjs, initMap)

start = time.time()
finalState = simulated_annealing(0.995, initSol, buildingProjs)
end = time.time()
print(finalState.score)
print_map(finalState)
print(end - start)

start = time.time()
finalState = hill_climbing(deepcopy(initSol), buildingProjs)
end = time.time()
print(finalState.score)
print(end - start)

print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

start = time.time()
finalState = steepest_ascent(deepcopy(initSol), buildingProjs)
end = time.time()
print(finalState.score)
print(end - start)

""" print("\n\n#2")

start = time.time()
finalState = hill_climbing(deepcopy(initSol), buildingProjs)
end = time.time()
print(finalState.score)
print(end - start)

print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

start = time.time()
finalState = steepest_ascent(deepcopy(initSol), buildingProjs)
end = time.time()
print(finalState.score)
print(end - start)

print("\n\n#3")

start = time.time()
finalState = hill_climbing(deepcopy(initSol), buildingProjs)
end = time.time()
print(finalState.score)
print(end - start)

print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

start = time.time()
finalState = steepest_ascent(deepcopy(initSol), buildingProjs)
end = time.time()
print(finalState.score)
print(end - start)

print("\n\n#4")

start = time.time()
finalState = hill_climbing(deepcopy(initSol), buildingProjs)
end = time.time()
print(finalState.score)
print(end - start)

print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

start = time.time()
finalState = steepest_ascent(deepcopy(initSol), buildingProjs)
end = time.time()
print(finalState.score)
print(end - start)

print("\n\n#5")

start = time.time()
finalState = hill_climbing(deepcopy(initSol), buildingProjs)
end = time.time()
print(finalState.score)
print(end - start)

print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

start = time.time()
finalState = steepest_ascent(deepcopy(initSol), buildingProjs)
end = time.time()
print(finalState.score)
print(end - start) """

#print_map(finalState) """