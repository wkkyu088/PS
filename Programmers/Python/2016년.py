def solution(a, b):
    weeks = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return weeks[(sum(days[:a-1])+b)%7]