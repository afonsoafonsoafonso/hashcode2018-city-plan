class BuildingProj:
    def __init__(self, id, type, rows, cols, attribute, plan):
        self.id = id
        self.type = type
        self.rows = int(rows)
        self.cols = int(cols)
        self.attribute = int(attribute)
        self.plan = plan