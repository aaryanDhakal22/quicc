def calculate_night_hours(schedule):
    night_hours = 0

    for entry in schedule:
        start_time, end_time = entry
        if start_time < 22:  # If shift starts before 10 PM
            start_time = 22  # Set start time to 10 PM (22 in 24-hour format)
        if end_time > 6:  # If shift ends after 6 AM
            end_time = 6  # Set end time to 6 AM

        if end_time > start_time:  # Valid working period
            night_hours += end_time - start_time

    return night_hours


# Test examples
# Example 1
schedule_1 = [(20, 23), (5, 8)]  # Shifts from 8 PM to 11 PM and 5 AM to 8 AM
night_hours_1 = calculate_night_hours(schedule_1)
print("Example 1 Night Hours Worked:", night_hours_1)

# Example 2
schedule_2 = [(22, 3), (4, 7)]  # Shifts from 10 PM to 3 AM and 4 AM to 7 AM
night_hours_2 = calculate_night_hours(schedule_2)
print("Example 2 Night Hours Worked:", night_hours_2)
