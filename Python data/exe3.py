from datetime import datetime

dt_with_microseconds = datetime.now()

dt_without_microseconds = dt_with_microseconds.replace(microsecond=0)

print("with microseconds:", dt_with_microseconds)
print("without microseconds:", dt_without_microseconds)