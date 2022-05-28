months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}


def compile_date(date):
    return [int(date[0:2]), int(date[3:5]), int(date[7:])]


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False


def is_past(day1, month1, day2, month2):
    if month1 > month2:
        return True
    if month1 == month2:
        return day1 > day2
    return False


def days_after_start(date):
    current_date = [1, 1]
    days = 0
    while current_date != date:
        if current_date[1] != date[1] and not is_past(current_date[0], current_date[1] + 1, date[0], date[1]):
            days += months[current_date[1]]
            current_date[1] += 1
        else:
            current_date[0] = 1 if current_date[0] == months[current_date[1]] else current_date[0] + 1
            current_date[1] += 1 if months[current_date[1]] == current_date[0] else 0


def days_calculator(start_date, end_date):
    days = 0

    return days


print(days_calculator('30/01/2022', '05/02/2022'))