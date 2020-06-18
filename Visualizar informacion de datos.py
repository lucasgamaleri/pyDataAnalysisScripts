# MORE DOCUMENTATION IN https://pandas.pydata.org
#getting started analyzing data in python

#check data types
df.dtypes()

#returns a statistical summary
df.describe()

df.describe(include="all")#provides full summary statistics
df[['column1','column2']].describe()

df.info() # shows the top 30 rows and bottom 30 rows of the dataframe

#you can set the columns to describe by

