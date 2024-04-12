from openpyxl import load_workbook
from time import sleep
from Employee import Employee
from Shift import Shift
from get_employees import get_employees
from pprint import pprint


workbook = load_workbook(filename="./xl_files/contents.xlsx")
sheet1 = workbook[" SCHED DEC04-10"]
col_names = [
    i.replace("\n", "") for i in open("col_names.txt", "r").readlines()
]

employee_list = get_employees(sheet1)

for employee in employee_list.keys():
    offset = 0
    emp = employee_list[employee]
    col_index = 1
    for cord in emp.xl_loc:
        row = cord[1:]
        while col_index < len(col_names):
            shift_name = sheet1[col_names[col_index + offset] + str(row)].value
            offset += 1

            if emp.name == "IRISH":
                print(shift_name, row, cord)
            if shift_name != None and shift_name != "None":
                date = sheet1[col_names[col_index + offset] + str(row)].value
                offset += 1
                period = sheet1[col_names[col_index + offset] + str(row)].value
                offset += 2
                reg_hr = sheet1[col_names[col_index + offset] + str(row)].value
                offset += 1
                night_diff = sheet1[
                    col_names[col_index + offset] + str(row)
                ].value
                offset += 1
                overtime = sheet1[
                    col_names[col_index + offset] + str(row)
                ].value
                if str(period[0]).isnumeric():
                    emp.add_shift(
                        Shift(
                            emp.name,
                            shift_name,
                            date,
                            period,
                            reg_hr,
                            night_diff,
                            overtime,
                            row,
                        )
                    )
            offset = 0
            col_index += 7
# for i in employee_list.keys():
#     print(len(employee_list[i].shifts))
employee_id = "IRISH"

print(employee_list[employee_id].shifts)
