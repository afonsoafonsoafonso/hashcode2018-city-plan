import sys
from city import City
from building_proj import BuildingProj
from building import Building
#USAGE: main input_file

def parse(file_name, buildings):
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

# main
file_name = sys.argv[1]
buildings = []
city = None

city = parse(file_name, buildings)

print(buildings)