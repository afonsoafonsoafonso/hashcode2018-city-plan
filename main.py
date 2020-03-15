import sys
from city import City
from building_proj import BuildingProj
from building import Building
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
    return best,nBest

# main
file_name = sys.argv[1]
buildingProjs = []
city = None

city = parse_file(file_name, buildingProjs)

for building in buildingProjs:
    print(building.type)

bestResidential, n = get_best_residential(buildingProjs)

print(bestResidential.cenas)
print(n)