import pandas as pd
import numpy as np
import csv


athletes = pd.read_csv("2025_Problem_C_Data/summerOly_athletes.csv")
country_codes = pd.read_csv("countries.csv", index_col=False)

NOC_dict = dict(zip(country_codes["NOC"], country_codes["Country"]))

