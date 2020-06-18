# MORE DOCUMENTATION IN https://pandas.pydata.org
#Example of adding recalculating and renaming a column
df["city-mpg"] = 235/df["city-mpg"]
df.rename(columns={"city_mpg":"city-L/100km"}, inplace=True)

#missing values
#drop N/A by deleting the whole row with a missing data
df.dropna()

df.dropna(subset=["column1"],axis=0,inplace=True) #axis=0 drops the entire row ; axis=1 drops entire column

#replace missing values
df.replace(missing_value, new_value)
#for example, we can replace missing data with the mean of the dataframe using:
mean = df["column1"].mean()
df["column1"].replace(np.nan, mean)

# To identify data types:
df.dtypes()

#To convert data types: 
df.astype()

#convert datatype to int in column "price"
df["price"] = df["price"].astype("int")

#rename columns:
#for example we need to convert meters per galoon to liters per hundred kilometers
# in car dataset

df["citi-mpg"]= 235/df["city-mpg"]
df.rename(columns={"city-mpg": "city-L/100km"}, inplace=True)