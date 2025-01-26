import numpy as np
import pandas as pd

'''
for country, year
- get data from programs
- get data from medals
- get data from athletes
- get data from hosts


export data as a numpy binary in the form
[[x1,y1],
[x2,y2],
...
[xn,yn]]

where 
xi = [
    NOC, 
    year, 
    #athletes, 
    #total athletes, 
    #countries, 
    #events, 
    #sports, 
    #disciplines, 
    first year competed, 
    #Olympics attended, 
    host
]
and
yi = [
    # golds
    # silvers
    # bronzes
    # total
]

A data point only exists IF a team competed that year



'''

# data that is just year dependent: num athletes, num countries, num events, num sports, host
# data that is year and country dependent: num athletes, 1st year, num olympics competed




# first, make a list of all NOC, year pairs


athlete_df = pd.read_csv('Clean Data/summerOly_athletes_cropped.csv', usecols=[0,3,4])
athlete_list = athlete_df.to_numpy(dtype=str)
print(athlete_list)

country_list = np.loadtxt('Clean Data/summerOly_countries_cropped.csv', delimiter=",", dtype=str)
medal_counts = np.loadtxt('Clean Data/summerOly_medals_clean.csv', delimiter=",", dtype=str, skiprows=1, usecols=[3,4,5,7,8])
# athlete_list = np.loadtxt('Clean Data/summerOly_athletes_cropped.csv', delimiter=",", skiprows=1, usecols=[0,3,4], dtype=[('Name', str), ('NOC', str), ('Year', int)])
# host_list = np.loadtxt('2025_Problem_C_Data/summerOly_hosts.csv', delimiter=',', dtype=str)

print(athlete_df)

# print(medal_counts)

competed_arr, num_athletes = np.unique(athlete_list[:,1:], axis=0, return_counts=True)

print(competed_arr)
print(competed_arr.shape)

# for i in competed_arr:





# print(competed_arr)

# print(competed_arr.shape)
# print(type(competed_arr))
# print(num_athletes.shape)
# data = np.column_stack((competed_arr, num_athletes))
# print(data)
# print(data.shape)