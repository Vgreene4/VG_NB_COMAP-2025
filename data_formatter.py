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

A data point only exists IF a team competed that year, otherwise there is none.

'''

# data that is just year dependent: num athletes, num countries, num events, num sports, host
# data that is year and country dependent: num athletes, 1st year, num olympics competed

# first, make a list of all NOC, year pairs


athlete_df = pd.read_csv('Clean Data/summerOly_athletes_cropped.csv', usecols=[0,3,4])
athlete_list = athlete_df.to_numpy(dtype=str)
# print(athlete_list)

country_list = np.loadtxt('Clean Data/summerOly_countries_cropped.csv', delimiter=",", dtype=str)
medal_counts = np.loadtxt('Clean Data/summerOly_medals_clean.csv', delimiter=",", dtype=str, skiprows=1, usecols=[3,4,5,6,7,8])
# athlete_list = np.loadtxt('Clean Data/summerOly_athletes_cropped.csv', delimiter=",", skiprows=1, usecols=[0,3,4], dtype=[('Name', str), ('NOC', str), ('Year', int)])
# host_list = np.loadtxt('2025_Problem_C_Data/summerOly_hosts.csv', delimiter=',', dtype=str)

programs_list = np.loadtxt('Clean Data/summerOly_programs_cropped.csv', delimiter=',', dtype=str)

print(programs_list.T)

# print(athlete_df)

# print(medal_counts)

competed_arr, num_athletes = np.unique(athlete_list[:,1:], axis=0, return_counts=True)

# print(competed_arr)

for i,row in enumerate(competed_arr):
    year, country = row[1], row[0]
    # print(num_athletes[i])
    print('country/year')
    print(row)
    # print(year)
    for e in programs_list.T:
        if e[0] == year:
            print("events/disciplines/sports")
            print(e[1:])

    score = [0,0,0,0]
    for e in medal_counts:
        if e[4] == year and e[5] == country:
            score = e[0:3]
    print('medals')
    print(score)
    print('\n')

# for row in competed_arr:
    # print(row)






# print(competed_arr)
# print(competed_arr.shape)

# for i in competed_arr:





# print(competed_arr)

# print(competed_arr.shape)
# print(type(competed_arr))
# print(num_athletes.shape)
# data = np.column_stack((competed_arr, num_athletes))
# print(data)
# print(data.shape)