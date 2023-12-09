#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 11:07:16 2023

Title: STA308 Final Exam

For each of the four census regions, compute the mean state percentage 
decrease (difference) in the flu-pneumonia mortality rates from 2018 to 2021 
((Rate2018 - Rate2021)/Rate2018*100), along with the corresponding standard 
deviation and coefficient of variationLinks to an external site.. Since both 
Alaska and Hawaii are geographically separated from the contiguous states, 
remove them from this analysis. The result of your program should be a table 
of numbers with 4 rows (corresponding to the four census regions) and 3 columns
of calculated values (the mean, standard deviation and coefficient of variation)
[note: your output will be 4 columns when considering the census region as a 
variable, but should contain only 3 columns of numbers).

@author: Will Paz
"""

#%%

import pandas as pd

## Data Entry

## The following line of code merge the four dataframes into one total dataframe

flu_2018 = pd.read_csv("https://tjfisher19.github.io/data/fluPneumonia_2018.csv")
flu_2018 = flu_2018.rename(columns={"State": "Code"}) # Changes the name of State to Code

flu_2021 = pd.read_csv("https://tjfisher19.github.io/data/fluPneumonia_2021.csv")

state_abb_codes = pd.read_csv("https://tjfisher19.github.io/data/state_abb_codes.csv")

census_regions = pd.read_csv("https://tjfisher19.github.io/data/censusRegions.csv")
census_regions = census_regions.rename(columns={"State": "Code"}) # Changes the name of State to Code

step1 = flu_2021.merge(state_abb_codes, on="State")
step1 = step1.rename(columns={"Rate": "Rate2021"}) # Changes the name of Rate to Rate2021

step2 = step1.merge(flu_2018,on="Code")
step2 = step2.rename(columns={"Rate": "Rate2018"}) # Changes the name of Rate to Rate2018

df = census_regions.merge(step2,on="Code") # The final dataframe


#%%

## Dataframe Management

flu_df = df[(df['Code'] != "AK") & (df['Code'] != "HI")] # "Filters" out Alaska and Hawaii

flu_df = flu_df[['Region', 'Rate2021', 'Rate2018']] # "Selects" the two rate columns and the region

flu_df = flu_df.assign(Pct_Dec = ((flu_df['Rate2018'] - flu_df['Rate2021']) /
                                  flu_df['Rate2018']) * 100) # "Mutate" to create a new varible
                                                             #  of the percent decrease from 2018 to 2021

flu_df = flu_df.groupby("Region")['Pct_Dec'].agg(['mean','std']) # "Summarizes" the mean and sd of Pct_Dec

flu_df = flu_df.assign(CoV = flu_df['std'] / flu_df['mean']) # "Mutate" a new varible, the coeff. of 
                                                             # variation (i.e. sd / mean)




