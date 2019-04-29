import pandas as pd
import numpy as np

data = pd.read_csv("dumm1.csv")

#print(data)

#print(data['Feature1'].corr(data['Feature2']))

#data.shape	=> number of rows and columns

Correlation_Coefficient = [[None for _ in range(data.shape[1])]for _ in range(data.shape[1])]	#list comprehension to create an empty 2d matrix

for i in range(0,data.shape[1]):
	for j in range(i,data.shape[1]):
		Correlation_Coefficient[i][j] = data[data.columns[i]].corr(data[data.columns[j]]) 		

#print(data.columns[0])	#method to extract a column name in string format

for i in range(0,len(Correlation_Coefficient[0])):
	print(Correlation_Coefficient[i])
	print("\n")