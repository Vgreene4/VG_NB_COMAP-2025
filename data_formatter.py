import numpy as np

'''
for country, year
- get data from programs
- get data from medals
- get data from athletes
- get data from hosts
'''


country_list = np.loadtxt('Clean Data/summerOly_countries_cropped.csv', delimiter=",", dtype=str)
medal_counts = np.loadtxt('Clean Data/summerOly_medals_counts_clean.csv', delimiter=",", dtype=str, skiprows=1)
athlete_list = np.loadtxt('Clean Data/summerOly_athletes_cropped.csv', delimiter=",", dtype=str, skiprows=1, usecols=[0,3,4])
host_list = np.loadtxt('2025_Problem_C_Data/summerOly_hosts.csv', delimiter=',', dtype=str)

print(host_list)