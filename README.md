# 2020-Election-Prediction
## Data Collection and Analysis
Most of the data was scraped from the FRED API using HTTP requests, so the dataset was already very clean. I used a heatmap to visualize the linear relationships between the variables before fitting a model.  
![Heatmap](https://i.imgur.com/0fKN1Fw.png)

## Models Used 
**K-Nearest Neighbors (KNN Regressor)**/
A KNN-R model was chosen because in I assumed that feature similarity existed for each year's election result. This would allow the KNN regreesor to make accurate predictions on out of sample data./
I first attempted to fit a KNN classifer model to the data and have the output a boolean of elected or not elected, but the problem I ran into was that the model returned false for both candidates this year. Given how close some elections have been this was not a surprise, but meant I had to shift my goal from a boolean output to a numerical one. 

**Random Forests Regressor**
I chose random forests regression (rf) because I wanted to use a different, more powerful technique (compared to KNN). I also kept in mind that rf has low bias and moderate variance.

## Model Predictions
![Predictions](https://i.imgur.com/5JhOKpj.png)

The Associated Press, at the time of writing this, says that President Elect Biden earned 50.7% of the popular vote. This means an error of .71% for the rf model and 1.81% for the knn model. Many polls had predictions in line with the knn model's, so the rf model performed very well.  


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
*$SPY Annual % Change* - Annual % Change of the S&P 500 Index (For election year this value is from January - September)\
*Dem Vote %* - Vote share of the democratic party presidential nominee\
**Source: FRED*
