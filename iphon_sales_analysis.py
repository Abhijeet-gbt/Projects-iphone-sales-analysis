import pandas as pd               
import seaborn as sns           
import matplotlib.pyplot as plt                  

df = pd.read_csv("iphone_resale_market_intelligence_usa_2026.csv")
print(df)

df.size

print(df.isnull().sum())
print(df.dropna(subset=["us_state","itemLocation"],inplace=True))
print(df.isnull().sum())

print(df.dtypes)

df["wasPrice"].fillna(df["wasPrice"].mean(),inplace=True)
df["available"].fillna(df["available"].mean(),inplace=True)
df["storage_gb_numeric"].fillna(df["storage_gb_numeric"].mean(),inplace=True)
df["sold"].fillna(df["sold"].mean(),inplace=True)
df["price_discount_pct"].fillna(df["price_discount_pct"].mean(),inplace=True)

df["storage_options_gb"] = df["storage_options_gb"].fillna(df["storage_options_gb"].mode()[0])
df["lastUpdated"] = df["lastUpdated"].fillna(df["lastUpdated"].mode()[0])
print(df.isnull().sum())

print(df[["storage_options_gb","lastUpdated"]])

print(df.head(10))
print(df.duplicated().sum())
print(df.drop_duplicates())


df["lastUpdated"] = pd.to_datetime(df["lastUpdated"])
df["year"] = df["lastUpdated"].dt.year
df["year"].fillna(df["year"].mode()[0], inplace=True)
df["year"] = df["year"].astype(str)

top_expensive_iphones = df.groupby("model_family")["price"].mean().sort_values(ascending=False)
print(top_expensive_iphones)

state_wise_price_variation = df.groupby("us_state")["price"].mean().sort_values(ascending=False)
print(df)

sns.lineplot(data=df,x="year",y="price",estimator="mean")
plt.title("Average iphone resale price over years")
plt.tight_layout()
plt.savefig("Average iphone resale price over years.png",dpi = 600,bbox_inches = "tight")
plt.show()

print(df["storage_gb_numeric"].astype(int))

sns.histplot(df["price"],bins=30,kde=True)
plt.title("Distribution of iphone prices")
plt.xlabel("Price")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("Distribution of iphone prices.png",dpi = 600,bbox_inches = "tight")
plt.show()

print(df["storage_gb_numeric"].value_counts())
df["storage_gb_numeric"] = df["storage_gb_numeric"].astype(int)

print(df.dtypes)

sns.barplot(data=df,x="storage_gb_numeric",y="price")
plt.title("Storage(GB) Vs Prices")
plt.tight_layout()
plt.savefig("Storage(GB) Vs Prices.png",dpi = 600,bbox_inches = "tight")
plt.show()


print(df.head(10))

sns.barplot(y="model_family",x="price",data=df,palette="Set2",hue="year")
plt.title("All iPhones model Average prices over years",fontsize = 14)
plt.xlabel("Prices",fontsize = 14)
plt.ylabel("Models",fontsize = 14)
plt.tight_layout()
plt.savefig("All iPhones model Average prices over years.png",dpi = 600,bbox_inches = "tight")
plt.show()

sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.tight_layout()
plt.savefig("Correlation.png",dpi = 600,bbox_inches = "tight")
plt.show()