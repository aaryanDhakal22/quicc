from datetime import datetime
from dateutil import tz
from org_assign import org_name


# 10 pm - 6 am : night difference
class Shift:
    def __init__(
        self, employee, day, date, period, reg_hr, night_diff, overtime, row
    ):
        self.employee = employee
        self.organization = org_name(int(row))
        self.day = day
        self.date = str(date).split(" ")[0][5:]
        self.period = period
        self.ph_start = self.get_start()
        self.ph_end = self.get_end()
        self.us_start = self.ph_start.astimezone(tz.gettz("US/Eastern"))
        self.us_end = self.ph_end.astimezone(tz.gettz("US/Eastern"))
        self.reg_hr = reg_hr
        self.night_diff = night_diff
        self.overtime = overtime
        self.total_hours = self.reg_hr + self.night_diff + self.overtime

    def get_start(self):
        month = str(self.date).split("-")
        # print("month", month)
        month, day = str(self.date).split("-")
        start, end = str(self.period).split(" - ")
        mer = start[-2:]
        hour = start.split(":")[0]
        hour = int(hour) if mer == "AM" else int(hour) + 12
        start_time = datetime(
            2023 if month == "12" else 2024,
            int(month),
            int(day),
            hour,
            int(start.split(":")[1][:-3]),
            tzinfo=tz.gettz("Asia/Manila"),
        )
        return start_time

    def get_end(self):
        month, day = str(self.date).split("-")
        start, end = str(self.period).split(" - ")
        mer = end[-2:]
        hour = end.split(":")[0]
        hour = int(hour) if mer == "AM" else int(hour) + 12
        end_time = datetime(
            2023 if month == "12" else 2024,
            int(month),
            int(day),
            int(end.split(":")[0]),
            int(end.split(":")[1][:-3]),
            tzinfo=tz.gettz("Asia/Manila"),
        )

        # ACCOUNT FOR DAY CHANGE
        if end[-2:] == "AM" and end_time.hour < self.ph_start.hour:
            end_time = end_time.replace(day=int(day) + 1)

        return end_time

    def get_hours(self):
        hours = self.ph_end - self.ph_start
        hours = hours.seconds / 3600
        return hours

    def night_hours(self):
        # return the number of hours that the shift has which is between
        pass

    def __repr__(self) -> str:
        return (
            self.employee
            + " "
            + str(self.date)
            + " "
            + str(self.us_start)
            + "-"
            + str(self.us_end)
            + " at "
            + str(self.organization)
        )
