#import building_proj

class Building:
    # talvez mudar para receber um building proj + locR e locC ???
    # locR e locC: row e col em que o building vai ser construido,
    def __init__(self, buildingProj, locR, locC):
        self.type = buildingProj.type
        self.rows = buildingProj.rows
        self.cols = buildingProj.cols
        self.cenas = buildingProj.cenas
        self.plan = buildingProj.plan
        self.locR = locR
        self.locC = locC
        self.services = []