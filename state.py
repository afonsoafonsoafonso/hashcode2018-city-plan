from city import City
from building_proj import BuildingProj
from building import Building
from copy import deepcopy

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
                            if self.calcManhattanDist(prow+mrow, pcol+mcol, nrow, ncol) > walkd:
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
                                        if foundBuilding.cenas not in buildings[len(buildings)-1].services and foundBuilding.cenas not in services:
                                            #services.append(foundBuilding.cenas)
                                            buildings[len(buildings)-1].services.append(foundBuilding.cenas)
                                            score += buildingProj.cenas
        return score
                
    def calcManhattanDist(self, row1, col1, row2, col2):
        return ( abs(row2 - row1) + abs(col2 - col1) )
