# sta308_final_exam

### Author: Will Paz

## The Prompt

Each year, the Center for Disease Control & Prevention (CDC) monitors the rates of infectious diseases across the United States. You are likely familiar with all the data collected about SARS-CoV-2 (COVID-19) since it impacted our lives for several years. However, this is only one aspect of the data the CDC collects. Each year they monitor the rates of infection for the seasonal Influenza virus, and Pneumonia cases. The 2017-2018 flu season (approximately December '17 through March '18) is noteworthy for being one of the worst flu seasons in recent history. Meanwhile, the 2020-2021 flu season was impacted by COVID-19 mitigation efforts (i.e., it happened before COVID vaccines were widely available, so many folks were still in masks when inside in public, schools continued with remote learning, people avoided crowded public places, etc...) and tended to have low rates.

The file fluPneumonia_2018.csv contains the mortality rate (deaths per 100,000) for flu and pneumonia cases in each state in 2018. The file fluPneumonia_2021.csv provides the mortality rate in 2021. The file state_abb_codes.csv provides a mapping of states & districts in the United States with their abbreviations, and the file censusRegions.csv provides a mapping of states and districts based to their geographical region as defined by the U.S. Census Bureau. 

For each of the four census regions, compute the mean state percentage decrease (difference) in the flu-pneumonia mortality rates from 2018 to 2021 ((Rate2018 - Rate2021)/Rate2018*100), along with the corresponding standard deviation and coefficient of variation. Since both Alaska and Hawaii are geographically separated from the contiguous states, remove them from this analysis. The result of your program should be a table of numbers with 4 rows (corresponding to the four census regions) and 3 columns of calculated values (the mean, standard deviation and coefficient of variation) [note: your output will be 4 columns when considering the census region as a variable, but should contain only 3 columns of numbers).

## Table from Analysis

| Region | Mean	| Standard Deviation |	Coefficient of Variation |
|--------|------|--------------------|-----------------------------|
| Midwest | 35.722549817265666 | 8.918304293133854 |	0.24965475137565343 |
| Northeast |	38.52744609696747 |	12.432945398732214 |	0.32270359596222553 |
| South | 24.86341831808104 |	7.140688471824784 |	0.28719657049859354 |
| West |	34.87706324940913 |	12.928896318087016 |	0.37069911034743014 |

## What is the Coefficient of Variation?

The coefficient of variation is a ratio between the standard deviation and mean. In general, this is showing the magnitude in which the variability of the data as it is related to the mean. Typically, it is used with vastly different means to create a fairly uniform way to make observations with.


## Analysis of the Data

First off, you can see that the northeast had the greatest percent difference in mortality rates from 2018 to 2021, and coming in second would be the midwest, and the west close behind them. The south exhibited by far the lowest mean difference in percentage of mortality. With that being said, when you account for the standard deviation, thus allowing us to use the coefficient of variation. The higher CV will be a larger dispersion of the variable, so we can see that the west has the most dispersion of mortality rate while the midwest has the least. I find this interesting because the midwest and west have similar means, but the standard deviation determines that there is more variation. Note that, the south had both the lowest mean and standard deviation. 


## R to Python Mapping Table

| Functionality | R	| Python |	
|---------------|---|--------|
| Chooses which rows we would like to keep/remove  | filter() | df[df["Column"] = ["Row1","Row2",...,"Rown"]] |
| Selects the desired columns |	select() | df[["Col1","Col2",...,"Coln"]] |	
| Creates groups based on the each unique element with the variable being grouped | group_by() |	df.groupby() (can be used with summarization) |	
| Adds or changes a new variable to the dataframe |	mutate() |	df.assign() |
| Summarizes the desired variables |	summarize() | df.groupby("Col1")["Col2"].agg[] |	

## Review of Course

In all, I would have to say that my favorite topic would be our project where we simulated the end of a basketball game. I found that fascination and the using logical statements is quite enjoyable. But, in all, I really enjoyed the course and I feel like I learned a lot.




