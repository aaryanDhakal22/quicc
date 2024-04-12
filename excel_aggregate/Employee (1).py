class Employee:
    def __init__(self, name):
        self.name = name
        self.xl_loc = []
        self.shifts = []
        self.reg_hr = 0
        self.night_diff = 0
        self.overtime = 0
        self.total_hours = 0
        self.org_log = dict()

    def add_loc(self, loc):
        self.xl_loc.append(loc)

    def add_shift(self, shift):
        self.reg_hr += shift.reg_hr
        self.night_diff += shift.night_diff
        self.overtime += shift.overtime
        self.total_hours += shift.total_hours
        
        self.shifts.append(shift)

    def __repr__(self) -> str:
        return str(self.name) + "\t" + "---".join(self.xl_loc)
