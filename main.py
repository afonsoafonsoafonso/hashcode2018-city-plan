import sys
from city import City
from building import Building

#USAGE: main input_file  

file_name = sys.argv[1]
buildings = []

try:
    with open(file_name, 'r') as input_file:
        vars = input_file.readline().split()
        city = City(vars[0], vars[1], vars[2], vars[3])
        #print(vars)

        for line in input_file:
            #print(line)
            plan = []
            vars = line.split()
            for nrow in range(int(vars[1])):
                row = input_file.readline()
                row = row.rstrip('\n')
                plan.append(row)
            print(plan)
            buildings.append(Building(vars[0], vars[1], vars[2], vars[3], plan))

    input_file.close()    
except:
    print("Error opening or parsing file.")
    raise SystemExit

for building in buildings:
    print(building)