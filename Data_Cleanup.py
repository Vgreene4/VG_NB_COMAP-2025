import pandas as pd
import numpy as np


athletes = pd.read_csv("Clean Data/summerOly_athletes_clean.csv")
country_list = pd.read_csv("Clean Data/countries.csv", index_col=False)
NOC_list = country_list["NOC"]

def remove_pre_ww1 (athletes):
    post_ww1 = athletes[athletes.Year >= 1920].copy()
    post_ww1.sort_values(by=['Year', 'NOC'], inplace=True, ignore_index=True)
    return post_ww1

def count_years (athletes, NOC_list):
    count_dict = dict()
    for code in NOC_list:
        country_data = athletes[athletes.NOC == code]
        years = country_data["Year"].unique()
        count_dict[code] = years
    return count_dict

def drop_countries (threshold, athlete_list, country_list):
    drop_list = []
    count_dict = count_years(athlete_list, country_list['NOC'])
    for country, count in count_dict.items():
        if len(count) <= threshold:
            drop_list.append(country)
    drop_list.sort()
    for code in drop_list:
        country_list = country_list[country_list.NOC != code]
        athlete_list = athlete_list[athlete_list.NOC != code]
    country_list.sort_values(by=['NOC'], inplace=True, ignore_index=True)
    athlete_list.sort_values(by=['Year', 'NOC'], inplace=True, ignore_index=True)
    return athlete_list, country_list, drop_list

athletes_post_ww1 = remove_pre_ww1(athletes)

clean_athletes, clean_countries, drop_list = drop_countries(1, athletes_post_ww1, country_list)

clean_athletes.to_csv('Clean Data/summerOly_athletes_cropped.csv', index=False)
clean_countries.to_csv('Clean Data/summerOly_countries_cropped.csv', index=False)










'''
Takes in the athletes file and the list of countries/NOC names we found online,
and replaces the names in the athletes file to reflect the countries list, also
sorts the athletes file first on year, and then on country. Saves the new file 
and the changes as CSV files
'''


'''

country_codes = pd.read_csv("countries.csv", index_col=False)

NOC_dict = dict(zip(country_codes["NOC"], country_codes["Country"]))

athletes_array = athletes.to_numpy(dtype=str)

changes_array = np.array(['Old Team Name', 'New Team Name', 'NOC'], dtype=str)

for row in athletes_array:
    if row[2] != NOC_dict[row[3]]:
        change = np.array([row[2],NOC_dict[row[3]],row[3]], dtype=str)
        changes_array = np.vstack((changes_array, change))
        row[2] = NOC_dict[row[3]]


changes_unique = np.unique(changes_array, axis=0)

athletes_df = pd.DataFrame(athletes_array)
athletes_df.columns = ["Name","Sex","Team","NOC","Year","City","Sport","Event","Medal"]

athletes_df.sort_values(by=['Year', 'NOC'], inplace=True, ignore_index=True)


print(athletes_df)

np.savetxt("name_changes.csv", changes_unique, fmt="%s", delimiter=",")
athletes_df.to_csv('summerOLY_athletes_clean.csv', index=False)

'''



