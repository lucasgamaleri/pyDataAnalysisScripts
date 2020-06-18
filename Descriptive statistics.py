#Exploratory data

#descriptive statistics od DataFrame "df"
df.describe()

#Summarize categorical data by using the value_contents method
drive_wheels_counts = df["drive-wheels"].values_counts()


#BoxPlot
sns.boxplot(x= "drive-wheels", y="prices", data=df)

#Scatterplot
y = df["engine-size"]
x = df["price"]
plt.scatter(x,y)

plt.title("Scatterplot of Engine Size vs Price")
plt.xlabel("Engine Size")
plt.ylabel("Price")

#GroupBy
df_test = df["drive-wheels", "body-style","price"]
df_grp = df_test.GroupBy(["drive-wheels","body-style"], as_index =False).mean()

#Pivot method to make table more legible
df_pivot = df_grp.Pivot(index="drive-wheels", columns="body-style")

#Heatmap plot: plot target variable over multiple variables
plt.pcolor(df_pivot,cmap="RdBBu")
plt.colorbar()
plt.show()

#Correlation
sns.regplot(x ="highway-mpg", y="prices", data=df)
plt.ylim(0,)
