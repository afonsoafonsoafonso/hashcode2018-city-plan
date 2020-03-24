from city import City
from building_proj import BuildingProj
from building import Building
from copy import deepcopy
from utils import remove_from_map

class State:
    def __init__(self, city, buildings, map, score):
        self.city = city
        self.buildings = deepcopy(buildings)
        self.map = deepcopy(map)
        self.score = score
        
    def nextState(self, buildingProj, mrow, mcol):
        newMap = deepcopy(self.map)
        newBuildings = deepcopy(self.buildings)
        newBuildings.append(Building(buildingProj, mrow, mcol))

        for prow in range(buildingProj.rows):
            for pcol in range(buildingProj.cols):
                if buildingProj.plan[prow][pcol] == '#':
                    if mrow + prow >= len(newMap) or mcol + pcol >= len(newMap[mrow + prow]):
                        return False
                    if newMap[mrow+prow][mcol+pcol] == '.':
                        newMap[mrow+prow][mcol+pcol] = len(self.buildings)+1
                    else:
                        return False
        newScore = self.calculateScore(self.city.walkDist, self.score, self.map, buildingProj, mrow, mcol, newBuildings)
        print("BUILDING SCORE=" + str(newScore - self.score))
        newBuildings[-1].score = newScore - self.score
        return State(self.city, newBuildings, newMap, newScore)

    def calculateScore(self, walkd, oldScore, map, buildingProj, mrow, mcol, buildings):
        visited = [] # edificios construidos já visitados 
        services = [] # servicos do edificio residencial que esta a ser construido ja encontrados
        score = oldScore # score a somar
        for prow in range(buildingProj.rows): # por cada row do projeto do edificio a construir
            for pcol in range(buildingProj.cols): # por cada col do projeto do edificio a construir
                if buildingProj.plan[prow][pcol] == '#': # caso exista uma celula ocupada do plano
                    for nrow in range(-walkd + (mrow + prow), walkd + (mrow+prow)+1): # cenas para aumentar a largura da pesquisa qd menor o comprimento
                        if nrow >= len(map) or nrow < 0:
                            continue
                        for ncol in range(-walkd + abs(nrow-mrow-prow) + pcol+mcol, walkd - abs(nrow-mrow-prow) + pcol + mcol + 1):
                            if ncol >= len(map[nrow]) or ncol < 0 :
                                continue
                            if map[nrow][ncol] != '.':
                                building_n = int(map[nrow][ncol])
                                if building_n not in visited: # index+1 do building no array dos buildings ja construidos
                                    visited.append(building_n)
                                    foundBuilding = buildings[building_n-1] #?
                                    if foundBuilding.type == 'R' and buildingProj.type == 'U':
                                        if buildingProj.cenas not in foundBuilding.services:
                                            foundBuilding.services.append(buildingProj.cenas)
                                            score += foundBuilding.cenas         
                                    elif foundBuilding.type == 'U' and buildingProj.type == 'R':
                                        if foundBuilding.cenas not in buildings[-1].services and foundBuilding.cenas not in services:
                                            #services.append(foundBuilding.cenas)
                                            buildings[-1].services.append(foundBuilding.cenas)
                                            score += buildingProj.cenas
        return score

    def remove_building(self, building):
        new_buildings = deepcopy(self.buildings)
        new_map = deepcopy(self.map)

        if isinstance(building, int): # if int: building == index
            removed = new_buildings[building]
            id = building
            del new_buildings[building]
        
        elif isinstance(building, Building): # if Building: building == object
            removed = building
            new_buildings.remove(building)

        new_score = self.score - removed.score
        new_map = remove_from_map(self.map, removed)

        return State(self.city, new_buildings, new_map, new_score)
