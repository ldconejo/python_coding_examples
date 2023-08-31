import math
import time

TIMES = 10000000

init = time.time()

for i in range(TIMES):
    value = math.sqrt(i * math.fabs(math.sin(i - math.cos(i))))

print("No function: %s" % (time.time() - init))

def calc_math(i):
    return math.sqrt(i * math.fabs(math.sin(i - math.cos(i))))

init = time.time()

for i in range(TIMES):
    value = calc_math(i)

print("Function: %s" % (time.time() - init))