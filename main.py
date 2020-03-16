import sys
import time
from city import City
from building_proj import BuildingProj
from building import Building
from state import State
#USAGE: main input_file

# returns city object. appends building projects to buildings
def parse_file(file_name, buildings):
    try:
        with open(file_name, 'r') as input_file:
            vars = input_file.readline().split()
            city = City(vars[0], vars[1], vars[2], vars[3])
            for line in input_file:
                plan = []
                vars = line.split()
                for nrow in range(int(vars[1])):
                    row = input_file.readline()
                    row = row.rstrip('\n')
                    plan.append(row)
                buildings.append(BuildingProj(vars[0], vars[1], vars[2], vars[3], plan))

        input_file.close()
        return city  
    except:
        print("Error opening or parsing file.")
        raise SystemExit

def get_best_residential(buildingProjs):
    max = 0
    n = 0
    nBest = 0
    best = None
    for building in buildingProjs:
        n = n + 1
        if building.type=='R':
            if building.ratio > max:
                best = building
                max = building.ratio
                nBest = n
    return best#,nBest

# main
start = time.time()

file_name = sys.argv[1]
buildingProjs = []
city = parse_file(file_name, buildingProjs)

# for building in buildingProjs:
#     if building.type=='R':
#         print(building.ratio)

bestResidential = get_best_residential(buildingProjs)

initMap = [['.' for col in range(city.cols)] for row in range(city.rows)]

State1 = State(city, [], initMap, 0)

State2 = State1.nextState(buildingProjs[100], 2, 2)

State3 = State2.nextState(buildingProjs[1], 3, 2)

State4 = State3.nextState(buildingProjs[1], 4, 4)

State5 = State4.nextState(buildingProjs[1], 5, 0)

end = time.time()
print(end - start)

print(State5.score)