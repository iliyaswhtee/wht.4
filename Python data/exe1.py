from datetime import datetime, timedelta

current_date = datetime.now()

new_date = current_date - timedelta(days=5)

print("Current Date:", current_date.strftime("%Y-%m-%d"))
print("New Date after subtracting:", new_date.strftime("%Y-%m-%d"))

#timedelta функция, которая возвращает объект продолжительности