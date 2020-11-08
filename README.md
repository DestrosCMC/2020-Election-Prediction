# 2020-Election-Prediction
## Data Collection and Analysis
Most of the data was scraped from the FRED API using HTTP requests, so the dataset was always very clean. I used a heatmap to visualize the linear relationships between the variables before fitting a model.  
![Heatmap](https://i.imgur.com/0fKN1Fw.png)

### Dataset Codebook
*Year* - Election Year\
*Name* - Candidate's Name\
*Q2 RGDPPC* - Q2 Real GDP Per Capita in chained 2012 dollars seasonally adjusted*\
*Unemp Rate* - Unemployment Rate of the United States in august of the election year*\
*Recession* - Indicator if an election occured during the election year*\
*Second Term* - If the candidate has been in office before, does not have to be consecutive\
*Repub Senate* - If the senate has a republican party majority\
*Democrat Senate* - If the senate has a democratic party majority\
*Q2 CPI* - Indicator of inflation* (FRED Code = CPIAUCSL)\
*Q2 Prod* - Industrial Production Index, Percent Change, Quarterly, Seasonally Adjusted*\
*$SPY Annual % Change* - Annual % Change of the S&P 500 Index (For election year this value is from January - September)
*Dem Vote %* - Vote share of the democratic party presidential nominee
*Source: FRED*
