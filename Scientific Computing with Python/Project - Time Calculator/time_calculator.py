def add_time(start, duration, day_of_week=''):
    ## Parse inputs
    start_hour = int(start.split()[0].split(':')[0])
    start_minute = int(start.split()[0].split(':')[1])
    am_pm = start.split()[1]

    duration_hour = int(duration.split(':')[0])
    duration_minute = int(duration.split(':')[1])

    ## Days of the week
    week = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    if day_of_week: start_day_index = week.index(day_of_week.lower())
    
    ## Add times
    total_days = 0
    end_hour = start_hour + duration_hour
    end_minute = start_minute + duration_minute
    while end_hour >= 11 or end_minute >= 60:
        if end_minute >= 60:
            end_hour += 1
            end_minute -= 60
        if end_hour >= 11:
            if am_pm == 'AM': am_pm = 'PM'
            else:
                am_pm = 'AM'
                total_days += 1
            if end_hour == 12: break
        if end_hour > 12:
            end_hour -= 12

    ## Display results
    new_time = f'{end_hour}:{str(end_minute).zfill(2)} {am_pm}'

    if day_of_week: new_time += ', ' + week[(start_day_index + total_days) % 7].capitalize()

    if total_days == 1: new_time += ' (next day)'
    if total_days > 1: new_time += f' ({total_days} days later)'

    return new_time

print(add_time("11:55 AM", "3:12"))