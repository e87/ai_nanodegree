# Modules can be used to organize functions, classes, and other data together in a structured way.

import random
import datetime

random_int = random.randint(1, 10)
print(random_int)

now = datetime.datetime.now()
print(now)
print(now.year)

print("Time Delta")
print(now + datetime.timedelta(days=22))
