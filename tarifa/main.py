import sys

data_plan = list(map(int, sys.stdin.readlines()))
data = data_plan[1] - sum(data_plan[1:]) + (len(data_plan) - 1) * data_plan[0]
print(data)
