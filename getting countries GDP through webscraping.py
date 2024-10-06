import pandas as pd
import numpy as np

#import the libraries as neccesary for analysis
#Then as we know the table we need is the 3rd one we will find and creat a database of it using pandas
#make sure to have lxml installed to read the formatted table

CountryGDP = pd.read_html(URL)

#as its the third table specify and save variable to element 

Gdp_table = CountryGDP[2]

#Now we replace coloumn headers with numbers for indexing  

Gdp_table.columns  = range(Gdp_table.shape[1])

#We want to simplify this tabe by only focusing on country names and GDP value 
print(Gdp_table)
Gdp_table = Gdp_table[[0,1]]

# Retaining only rows of top 10 economies utilsiing index 

Gdp_table = Gdp_table.iloc[1:11,:]

#Change coloumns to represent correct titles 

Gdp_table.columns = ['Country', 'GDP (Million USD)']


#CHeck these chnages are correct 

print(Gdp_table)