def split_time_str(time_str: str) -> tuple:
    """HELPER. Given a time in format xx:xx, x:x. or some variant, 
    returns a tuple (hours, minutes).
    Assumes time is properly formatted, and separator is ':' 
    """

    hours, minutes = time_str.split(":")
    return int(hours), int(minutes)


def days_later_segment(n: int) -> str:
    """HELPER. Given a n (number of days) returns a predefined string showing 
    how many days later we landed on after doing our calculations."""

    if n == 1:
        return " (next day)"
    elif n > 1:
        return f" ({n} days later)"
    return ""


def day_of_week_segment(start_day: str, n_days: int):
    """HELPER. Given a starting day and a number of days from that day,
    returns the day of the week we land after summing n days to start_day."""

    if start_day == "":
        return ""

    list_of_days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    day_index = list_of_days.index(start_day.title())
    n = (day_index + n_days) % 7
    return f", {list_of_days[n]}"


def split_time_segments(start_time: str) -> tuple:
    """HELPER. Given a start_time formated "xx:xx AM", 
    returns the AM/PM and the start_time segments as a tuple of strings"""

    return start_time.split(" ")[-1], start_time.upper()[:-2].strip()


def add_time(start: str, duration: str, start_day: str = ""):

    am_pm, start = split_time_segments(start)  # split start time information

    init_hour, init_min = split_time_str(start)
    delta_hour, delta_min = split_time_str(duration)

    hour = init_hour + delta_hour
    if am_pm == "PM":
        hour += 12

    minutes = init_min + delta_min
    if minutes > 59:
        minutes %= 60
        hour += 1

    n_days = hour // 24
    str_n_days = days_later_segment(n_days)
    str_day_of_the_week = day_of_week_segment(start_day, n_days)

    hour %= 24
    am_pm = "AM" if hour < 12 else "PM"

    hour = 12 if hour in [0, 12] else hour % 12

    return f"{hour}:{minutes:02d} {am_pm}{str_day_of_the_week}{str_n_days}"
