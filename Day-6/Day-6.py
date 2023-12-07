#%%
import functools
data = [
    {"time":40,
    "record_distance":215},
    {"time":92,
    "record_distance":1064},
    {"time":97,
    "record_distance":1505},
    {"time":90,
    "record_distance":1100},
]

total_possible_wins = []
for race in data:
    possible_wins = 0
    for t_held in range(0, race["time"]):
        time_left = race["time"] - t_held
        distance = t_held * time_left
        if distance > race["record_distance"]:
            possible_wins = possible_wins + 1
    total_possible_wins.append(possible_wins)

# %%
functools.reduce(lambda a,b: a*b,total_possible_wins) 
# %%
from sympy import *
# x - x^2 = dist

new_data = {
    "time": 40929790,
    "record_distance": 215106415051100
}

x = symbols('x')
roots = solve((x*new_data["time"] - x**2)-new_data["record_distance"] , x)
num_solutions = round(roots[1] - roots[0] + 1)



# %%
