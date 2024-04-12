from Employee import Employee


def get_employees(sheet):
    employee_list = dict()
    row = 1
    while True:
        # sleep(0.3)
        
        elem = sheet["A" + str(row)]
        if elem.value == "END":
            break
        if (
            elem != None
            and elem.value != None
            and elem.value.lower() != "name"
            and elem.value != " "
            and len(elem.value) > 1
        ):
            if elem.value not in employee_list.keys():
                employee_list.setdefault(elem.value, Employee(elem.value))
            employee_list[elem.value].add_loc("A" + str(row))
        row += 1
    return employee_list
