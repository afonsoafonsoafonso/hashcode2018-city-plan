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
        buildingId = len(self.buildings)+1
        newBuildings.append(Building(buildingProj, mrow, mcol, buildingId))

        for prow in range(buildingProj.rows):
            for pcol in range(buildingProj.cols):
                if buildingProj.plan[prow][pcol] == '#':
                    if mrow + prow >= len(newMap) or mcol + pcol >= len(newMap[mrow + prow]):
                        return False
                    if newMap[mrow+prow][mcol+pcol] == '.':
                        newMap[mrow+prow][mcol+pcol] =  buildingId
                    else:
                        return False
        newScore = self.calculateScore(self.city.walkDist, self.score, self.map, buildingProj, mrow, mcol, newBuildings)
        newBuildings[-1].score = newScore - self.score
        return State(self.city, newBuildings, newMap, newScore)

    def calculateScore(self, walkd, oldScore, map, buildingProj, mrow, mcol, buildings, index=-1):
        visited = [] # edificios construidos já visitados 
        services = [] # servicos do edificio residencial que esta a ser construido ja encontrados
        score = oldScore # score a somar
        selfBuildingId = buildings[index].buildingId
        for prow in range(buildingProj.rows): # por cada row do projeto do edificio a construir
            for pcol in range(buildingProj.cols): # por cada col do projeto do edificio a construir
                if buildingProj.plan[prow][pcol] == '#': # caso exista uma celula ocupada do plano
                    for nrow in range(-walkd + (mrow + prow), walkd + (mrow+prow)+1): # cenas para aumentar a largura da pesquisa qd menor o comprimento
                        if nrow >= len(map) or nrow < 0:
                            continue
                        for ncol in range(-walkd + abs(nrow-mrow-prow) + pcol+mcol, walkd - abs(nrow-mrow-prow) + pcol + mcol + 1):
                            if ncol >= len(map[nrow]) or ncol < 0 :
                                continue
                            if map[nrow][ncol] != '.' and map[nrow][ncol] != selfBuildingId:
                                building_n = int(map[nrow][ncol]) # index+1 do building no array dos buildings ja construidos
                                if building_n not in visited:
                                    visited.append(building_n)
                                    foundBuilding = buildings[building_n-1] #?
                                    if foundBuilding.type == 'R' and buildingProj.type == 'U':
                                        if buildingProj.cenas not in foundBuilding.services:
                                            foundBuilding.services.append(buildingProj.cenas)
                                            score += foundBuilding.cenas         
                                    elif foundBuilding.type == 'U' and buildingProj.type == 'R':
                                        if foundBuilding.cenas not in buildings[index].services and foundBuilding.cenas not in services:
                                            #services.append(foundBuilding.cenas)
                                            buildings[index].services.append(foundBuilding.cenas)
                                            score += buildingProj.cenas
        return score

    def replace_building(self, index, buildingProj):
        building = self.buildings[index]
        # vai se tentar construir building no mesmo sitio que o outro estava
        mrow = building.mrow
        mcol = building.mcol

        newMap = remove_from_map(self.map, building)

        # check if new building can replace the one to be replaced
        for prow in range(buildingProj.rows):
            for pcol in range(buildingProj.cols):
                if buildingProj.plan[prow][pcol] == '#':
                    if mrow + prow >= self.city.rows or mcol + pcol >=self.city.cols:
                        return False
                    if newMap[mrow+prow][mcol+pcol] == '.':
                        newMap[mrow+prow][mcol+pcol] = building.buildingId
                    else:
                        return False
        # copiar buildings e substituir building a ser substituito pelo novo mas com o mesmo buildingId
        newBuildings = deepcopy(self.buildings)
        newBuildings[index] = Building(buildingProj, mrow, mcol, building.buildingId)
        # calcular score usando a mesma cidade, tirando do score o contributo do edificio removido, etc etc e no fim 
        # parametro opcional para passar index do novo building na lista dos buildings
        newScore = self.calculateScore(self.city.walkDist, self.score - building.score, newMap, buildingProj, mrow, mcol, newBuildings, building.buildingId-1)
        newBuildings[index].score = newScore - (self.score - building.score)

        return State(self.city, newBuildings, newMap, newScore)
