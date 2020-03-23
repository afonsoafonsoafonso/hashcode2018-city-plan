import sys
import time
from city import City
from building_proj import BuildingProj
from building import Building
from state import State
from algorithms import *

#USAGE: python3 main.py input_file

def d_parse_file(file_name, optimizations):
    buildings = []
    bestUs = {}
    bestRindex = None
    i = 0
    bestR = None
    
    with open(file_name, 'r') as input_file:
        vars = input_file.readline().split()
        city = City(vars[0], vars[1], vars[2], vars[3])
        for line in input_file:
            i += 1
            plan = []
            vars = line.split()
            for nrow in range(int(vars[1])):
                row = input_file.readline()
                row = row.rstrip('\n')
                plan.append(row)
                building = BuildingProj(i, vars[0], vars[1], vars[2], vars[3], plan)
                if building.type == 'R':
                    if bestR == None:
                        bestR = building
                    elif building.ratio > bestR.ratio:
                        bestR = building
                elif building.type == 'U':
                    if building.cenas not in bestUs.keys():
                        bestUs[building.cenas] = building
                    elif building.rows * building.cols < bestUs[building.cenas].rows * bestUs[building.cenas].cols:
                        bestUs[building.cenas] = building
    input_file.close()
    return city, bestR, bestUs.values()

def parse_file(file_name):
    buildings = []
    i = 0 #235
    try:
        with open(file_name, 'r') as input_file:
            vars = input_file.readline().split()
            city = City(vars[0], vars[1], vars[2], vars[3])
            for line in input_file:
                i += 1
                plan = []
                vars = line.split()
                for nrow in range(int(vars[1])):
                    row = input_file.readline()
                    row = row.rstrip('\n')
                    plan.append(row)
                buildings.append(BuildingProj(i, vars[0], vars[1], vars[2], vars[3], plan))

        input_file.close()
        return city, buildings 
    except:
        print("Error opening or parsing file.")
        raise SystemExit
    
# main
start = time.time()

""" file_name = sys.argv[1]
city, bestR, bestUs = parse_file(file_name)
bestUs = list(bestUs)
bestUs.append(bestR)
buildingProjs = bestUs

initScore = 0
initMap = [['.' for col in range(city.cols)] for row in range(city.rows)]
initState = State(city, [], initMap, initScore) """

file_name = sys.argv[1]
city, buildingProjs = parse_file(file_name)
initMap = [['.' for col in range(city.cols)] for row in range(city.rows)]
initState = State(city, [], initMap, 0)


finalState = d_hill_climbing(initState, city, buildingProjs, initMap)
#finalState = d_steepest_ascent(initState, city, buildingProjs, initMap)
#finalState = d_hill_climbing_random(initState, city, buildingProjs, initMap)

print(finalState.score)
for rown in range(len(finalState.map)):
    print('\n', end='')
    for coln in range(len(finalState.map[0])):
        if finalState.map[rown][coln] == '.':
            print('....|', end='')
        else:
            print(finalState.buildings[int(finalState.map[rown][coln])-1].type, end='')
            print(str(finalState.map[rown][coln]).zfill(3), end='')
            print('|', end='')

print('\n')
end = time.time()
print(end - start)