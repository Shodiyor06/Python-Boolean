# task33.py
logged_in = input() == "True"
is_admin = input() == "True"
result = logged_in and not is_admin
print(result)