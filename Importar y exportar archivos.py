# MORE DOCUMENTATION IN https://pandas.pydata.org



#Importing pandas library
import pandas as pd

#Creating path as variable
url = "https://archive.ics.ucl.edu/ml/machine-learning-databases/autos/"

#importing the data
df = pd.read_csv(url)

# if there's not a header then
df = pd.read_csv(url, header = None)

#Take a look at the data
df #prints the entire dataframe (not recommended for large datasets)
df.head(n) #to show the first n rows of dataframe
df.tail(n) #shows the botton n rows of dataframe

#adding headers
headers = ["column1","column2","column3"]
df.columns = headers

#saving modified dataset
path = "C:\Windows\data.csv"
df.to_csv(path)

#other formats
pd.read_excel()
pd.read_json()
pd.read_sql()

df.to_excel()
df.to_json()
df.to_sql()
