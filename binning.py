# MORE DOCUMENTATION IN https://pandas.pydata.org

#grouping values into BINS
#converts numeric into categorical variables
#group a set of numerical values into a set of bins


#to create 3 categories, first we need 4 numbers as dividers
bins= np.linspace(min(df["price"]),max(df["price"]),4)
group_names = ["low", "medium","high"]
df["price-binned"] = pd.cut(df["price"],bins,labels= group_names, include_lowest=True)

#one-hot encoding to convert data to separated-column categories

pd.get_dummies(df["fuel"])