class Building:
    # mrow e mcol: row e col em que o building vai ser construido,
    def __init__(self, building_proj, mrow, mcol, building_id):
        #projId acaba por ser o index do buildingProject na lista dos buildingProjects
        #o buildingId é igual mas deste objecto building na lsita dos buildings
        self.projId = building_proj.id
        self.type = building_proj.type
        self.rows = building_proj.rows
        self.cols = building_proj.cols
        self.attribute = building_proj.attribute
        self.plan = building_proj.plan
        self.mrow = mrow
        self.mcol = mcol
        self.services = []
        self.score = None
        self.building_id = building_id

    def __eq__(self, other):
        if self.projId == other.projId and self.building_id == other.building_id:
            return True
        else:
             False