# task38.py
logged_in = input("Tizimga kirganmi? (True/False): ") == "True"
session_time = int(input("Sessiya vaqti: "))
print(not logged_in or session_time == 0)
