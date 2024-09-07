def add_time(start_time, duration, start_day=""):
    """
    Calculate the addition of a duration to a clock time

    Parameters
    ----------
    start_time : str
        12-hour clock format (ending in AM or PM)

    duration: str
        Number of hours and minutes

    start_day : str, optional
        Day of the week

    Returns
    -------
    str
        Addition of ``duration`` to ``start_time`` in 12-hour clock format

    Examples
    --------
    >>> add_time("11:43 AM", "00:20")
    2:02 PM, Monday
    >>> add_time("11:43 PM", "24:20", "tueSday")
    12:03 AM, Thursday (2 days later)

    """

    start_hours, start_period = start_time.split()

    # convert time to hrs
    start_hours = start_hours.split(":")
    start_hours = list(map(int, start_hours))
    if start_period == "PM":
        start_hours[0] = start_hours[0] + 12

    duration = duration.split(":")
    duration = list(map(int, duration))

    # calculate total time in mins
    start_mins = (start_hours[0] * 60) + start_hours[1]
    duration_mins = (duration[0] * 60) + duration[1]
    total_time_mins = start_mins + duration_mins

    # convert time in mins to HH:MM
    total_HH = total_time_mins // 60
    total_MM = total_time_mins % 60

    # calculate the day
    day_after = total_HH // 24
    day_HH = total_HH % 24

    # calculate final day of the week, after adding day_after
    if start_day:
        day_of_the_week = [
            "Sunday",
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thusday",
            "Friday",
            "Saturday",
        ]
        start_day = start_day.title()
        start_day_position = day_of_the_week.index(start_day)
        final_week_day_after_position = (start_day_position + day_after) % 7
        final_week_day_after = day_of_the_week[final_week_day_after_position]

    # calculate final output
    period = day_HH // 12  # am/pm
    final_HH = day_HH % 12
    if not final_HH:  # time at 0 == 12
        final_HH = 12
    final_MM = total_MM

    if period == 0:
        final_period = "AM"
    else:
        final_period = "PM"

    if day_after == 0:
        final_day_after = ""
    elif day_after == 1:
        final_day_after = "(next day)"
    else:
        final_day_after = f"({day_after} days later)"

    # determine added time
    added_time = str(final_HH) + ":" + str(final_MM).zfill(2) + " " + final_period
    if start_day:
        added_time = added_time + ", " + final_week_day_after
    if final_day_after:
        added_time = added_time + " " + final_day_after

    return added_time


print(add_time("3:00 PM", "3:10"))
# Returns: 6:10 PM

print(add_time("11:30 AM", "2:32", "Monday"))
# Returns: 2:02 PM, Monday

print(add_time("11:43 AM", "00:20"))
# Returns: 12:03 PM

print(add_time("10:10 PM", "3:30"))
# Returns: 1:40 AM (next day)

print(add_time("11:43 PM", "24:20", "tueSday"))
# Returns: 12:03 AM, Thursday (2 days later)

print(add_time("6:30 PM", "205:12"))
# Returns: 7:42 AM (9 days later)
