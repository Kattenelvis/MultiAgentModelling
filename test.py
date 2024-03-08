import random
from math import floor

t = [1,1,0]
t[floor(random.uniform(0,3))] = 2

print(t)