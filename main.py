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
"""
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

start = time.time()
final_state = tabuSearchWithAnnealing(20, 0.995, deepcopy(init_sol), building_projs)
end = time.time()
print(final_state.score)
print(end - start)

print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

start = time.time()
final_state = tabuSearch(20, 500, deepcopy(init_sol), building_projs)
end = time.time()
print(final_state.score)
print(end - start)"""
"""
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

print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
"""

"""
#GENETIC ALGORITHM LINDOOO
init_sol1 = getRandomSolution(empty_state, city, building_projs, init_map)
init_sol2 = getRandomSolution(empty_state, city, building_projs, init_map)
print("Parent0: "+ (str)(init_sol.score))
print("Parent1: " + (str)(init_sol1.score))
print("Parent2: " + (str)(init_sol2.score))
sols = []
sols.append(init_sol)
sols.append(init_sol1)
sols.append(init_sol2)
start = time.time()
final_state = genetic(deepcopy(sols), 40, building_projs, 5)
end = time.time()
print("Final Score: " + (str)(final_state.score))
print("Time: " + (str)(end - start))
"""


print("Initial Solution: "+ (str)(init_sol.score))
start = time.time()
final_state = swarm(5000, 2, deepcopy(init_sol), building_projs)
end = time.time()
print("Start Score: " + (str)(init_sol.score))
print("Final Score: " + (str)(final_state.score))
print("Time: " + (str)(end - start))