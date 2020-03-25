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
city, building_projs = parseFile(file_name)
init_map = [['.' for col in range(city.cols)] for row in range(city.rows)]
empty_state = State(city, [], init_map, 0)
init_sol = getRandomSolution(empty_state, city, building_projs, init_map)

""" start = time.time()
final_state = tabuSearch(15, init_sol, building_projs)
end = time.time()
print(final_state.score)
#print_map(final_state)
print(end - start)

print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

start = time.time()
final_state = tabuSearch(30, init_sol, building_projs)
end = time.time()
print(final_state.score)
#print_map(final_state)
print(end - start)

print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

start = time.time()
final_state = tabuSearch(50, init_sol, building_projs)
end = time.time()
print(final_state.score)
#print_map(final_state)
print(end - start)

print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

start = time.time()
final_state = simulatedAnnealing(0.995, init_sol, building_projs)
end = time.time()
print(final_state.score)
#print_map(final_state)
print(end - start) """

print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

start = time.time()
final_state = hillClimbing(deepcopy(init_sol), building_projs)
end = time.time()
print(final_state.score)
print(end - start)

print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

start = time.time()
final_state = steepestAscent(deepcopy(init_sol), building_projs)
end = time.time()
print(final_state.score)
print(end - start)

print("\n\n#2")

start = time.time()
final_state = hillClimbing(deepcopy(init_sol), building_projs)
end = time.time()
print(final_state.score)
print(end - start)

print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

start = time.time()
final_state = steepestAscent(deepcopy(init_sol), building_projs)
end = time.time()
print(final_state.score)
print(end - start)

print("\n\n#3")

start = time.time()
final_state = hillClimbing(deepcopy(init_sol), building_projs)
end = time.time()
print(final_state.score)
print(end - start)

print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

start = time.time()
final_state = steepestAscent(deepcopy(init_sol), building_projs)
end = time.time()
print(final_state.score)
print(end - start)

print("\n\n#4")

start = time.time()
final_state = hillClimbing(deepcopy(init_sol), building_projs)
end = time.time()
print(final_state.score)
print(end - start)

print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

start = time.time()
final_state = steepestAscent(deepcopy(init_sol), building_projs)
end = time.time()
print(final_state.score)
print(end - start)

print("\n\n#5")

start = time.time()
final_state = hillClimbing(deepcopy(init_sol), building_projs)
end = time.time()
print(final_state.score)
print(end - start)

print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

start = time.time()
final_state = steepestAscent(deepcopy(init_sol), building_projs)
end = time.time()
print(final_state.score)
print(end - start)