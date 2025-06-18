# task38.py
logged_in = input() == "True"
session_time = int(input())
result = not logged_in or session_time == 0
print(result)