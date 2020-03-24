import sys
import time
from city import City
from building_proj import BuildingProj
from building import Building
from state import State
from algorithms import *
from utils import *

#USAGE: python3 main.py input_file
    
start = time.time()

file_name = sys.argv[1]
city, buildingProjs = parse_file(file_name)
initMap = [['.' for col in range(city.cols)] for row in range(city.rows)]
initState = State(city, [], initMap, 0)

#finalState = hill_climbing(initState, city, buildingProjs, initMap)
finalState = d_steepest_ascent(initState, city, buildingProjs, initMap)
#finalState = d_hill_climbing_random(initState, city, buildingProjs, initMap)

print_map(finalState)

print('\n')
end = time.time()
print(end - start)

print_map(finalState.remove_building(finalState.buildings[0]))
