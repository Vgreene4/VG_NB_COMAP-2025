import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

countries = np.loadtxt("Clean Data/countries.csv", dtype=str, delimiter=",")
medals = np.loadtxt("Clean Data/summerOly_medals_counts_clean.csv", dtype=str, delimiter=",")


def graphCountry(country, medal_list):
    indiv_country = np.array([x for x in medal_list if x[1]==country])
    print(indiv_country)

    year, gold, silver, bronze = indiv_country.T[6].astype(int), indiv_country.T[4].astype(int), indiv_country.T[3].astype(int), indiv_country.T[2].astype(int)

    plt.bar(year, gold, color='yellow', width=2.5)
    plt.bar(year, silver, color='gray', bottom=gold, width=2.5)
    plt.bar(year, bronze, color='brown', bottom=silver+gold, width=2.5)
    plt.title(country)
    plt.xlim(1892,2028)
    plt.xticks(np.arange(1896, 2028, 4), rotation=-70)

    plt.show()



graphCountry('France', medals)

