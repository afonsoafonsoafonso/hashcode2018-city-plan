class Building:
    # locR e locC: row e col em que o building vai ser construido,
    def __init__(self, buildingProj, mrow, mcol, buildingId):
        self.projId = buildingProj.id
        self.type = buildingProj.type
        self.rows = buildingProj.rows
        self.cols = buildingProj.cols
        self.cenas = buildingProj.cenas
        self.plan = buildingProj.plan
        self.mrow = mrow
        self.mcol = mcol
        self.services = []
        self.score = None
        self.buildingId = buildingId

    def __eq__(self, other):
        if self.projId == other.projId and self.buildingId == other.buildingId:
            return True
        else:
             False