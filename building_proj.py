class BuildingProj:
    def __init__(self, type, rows, cols, cenas, plan):
        self.type = type
        self.rows = int(rows)
        self.cols = int(cols)
        self.cenas = int(cenas)
        self.plan = plan
        if type=='R':
            self.ratio = int(cenas)/(int(rows)*int(cols))
        else:
            self.ratio = None