from datetime import datetime

def date_difference_in_seconds(date1, date2):
    date_format = "%Y-%m-%d %H:%M:%S"
    datetime1 = datetime.strptime(date1, date_format)
    datetime2 = datetime.strptime(date2, date_format)
    
    difference = datetime2 - datetime1
    difference_in_seconds = difference.total_seconds()
    
    return difference_in_seconds

date1 = "2022-01-01 00:00:00"
date2 = "2022-01-02 12:30:15"

print("Difference in seconds:", date_difference_in_seconds(date1, date2))