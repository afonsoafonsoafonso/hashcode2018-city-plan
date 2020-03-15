from city import City
from building_proj import BuildingProj
from building import Building
from copy import deepcopy

class State:
    def __init__(self, city, buildings, map):
        self.city = city
        self.buildings = deepcopy(buildings)
        self.map = deepcopy(map)
        # falta criar lista de lsitas com o mapa todo consoante os buildings

    # cria um novo estado e adiciona building ao mapa
    def nextState(self, buildingProj, mrow, mcol):
        newMap = self.map.deepcopy()
        newBuildings = deepcopy(self.buildings).append(Building(buildingProj, mrow, mcol))

        for prow in range(buildingProj.rows):
            for pcol in range(buildingProj.cols):
                if(buildingProj.plan[prow][pcol]=='#'):
                    newMap[mrow+prow][mcol+mcol] = len(self.buildings)+1

        return State(city, newBuildings, newMap)
                
        