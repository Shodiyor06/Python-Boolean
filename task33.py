# task33.py
logged_in = input("Tizimga kirganmi? (True/False): ") == "True"
is_admin = input("Adminmi? (True/False): ") == "True"
print(logged_in and not is_admin)
