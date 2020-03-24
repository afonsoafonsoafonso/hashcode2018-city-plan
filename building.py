class Building:
    # locR e locC: row e col em que o building vai ser construido,
    def __init__(self, buildingProj, locR, locC):
        self.projId = buildingProj.id
        self.type = buildingProj.type
        self.rows = buildingProj.rows
        self.cols = buildingProj.cols
        self.cenas = buildingProj.cenas
        self.plan = buildingProj.plan
        self.locR = locR
        self.locC = locC
        self.services = []
        self.score = None

    def __eq__(self, other):
        if self.projId == other.projId and self.locR == other.locR and self.locC == other.locC:
            return True
        else:
             False