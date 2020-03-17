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
State = State(city, [], initMap, 0)
State = State.nextState(buildingProjs[99], 0, 0)

State = State.nextState(buildingProjs[101], 2, 0)

State = State.nextState(buildingProjs[101], 2, 3)


"""
State1 = State(city, [], initMap, 0)
State2 = State1.nextState(buildingProjs[100], 2, 2)
State3 = State2.nextState(buildingProjs[1], 200, 200)
State4 = State3.nextState(buildingProjs[1], 123, 543)
State5 = State4.nextState(buildingProjs[1], 129, 590)
State6 = State5.nextState(buildingProjs[1], 123, 965)
State7 = State6.nextState(buildingProjs[1], 14, 740)
State8 = State7.nextState(buildingProjs[1], 90, 500)
State9 = State8.nextState(buildingProjs[1], 678, 912)
State10 = State9.nextState(buildingProjs[1], 405, 45)
State11 = State10.nextState(buildingProjs[1], 905, 123)
"""
""" states = []
states.append(State(city, [], initMap, 0))
for i in range(1,200):
    states.append(states[i-1].nextState(buildingProjs[i-1], i, i))
    #states[i] = states[i-1].nextState(buildingProjs[i]) """



    


end = time.time()
print(end - start)
print(State.score)
#print(states[].score)