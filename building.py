import building_proj

class Building(building_proj.BuildingProj):
    # locR e locC: row e col em que o building vai ser construido, respetivamente
    def __init__(self, type, rows, cols, cenas, plan, locR, locC):
        super().__init__(type, rows, cols, cenas, plan)
        self.locR = locR
        self.locC = locC