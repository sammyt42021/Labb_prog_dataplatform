import pandas as pd


# 1. EXTRACT (Read file)

df = pd.read_csv("data/products.csv", sep=";")

print("Raw data:")
print(df)



# 2. CLEAN STRING COLUMNS

# Clean ID
df["id"] = df["id"].str.strip().str.upper()

# Clean name
df["name"] = df["name"].str.strip().str.title()

# Clean currency
df["currency"] = df["currency"].str.strip().str.upper()



# 3. SAFE TYPE CONVERSION

df["price"] = pd.to_numeric(df["price"], errors="coerce")

df["created_at"] = (
    df["created_at"]
    .astype(str)
    .str.strip()
    .str.replace("/", "-", regex=False)
)

df["created_at"] = pd.to_datetime(
    df["created_at"],
    errors="coerce",
    yearfirst=True
)



# 4. FLAG MISSING VALUES


df["id_missing"] = df["id"].isna() | (df["id"] == "")
df["price_missing"] = df["price"].isna()
df["currency_missing"] = df["currency"].isna() | (df["currency"] == "")
df["zero_price"] = df["price"] == 0
df["negative_price"] = df["price"] < 0
df["extreme_price"] = df["price"] > 10000

print("\nData with flags:")
print(df)


# 5. DEFINE REJECTION RULES

reject_condition = (
    df["id_missing"] |
    df["price_missing"] |
    df["currency_missing"] |
    df["negative_price"]
)

df_rejected = df[reject_condition].copy()
df_valid = df[~reject_condition].copy()



# 6. ADDING REJECTION REASONS

df_rejected["reason"] = ""

df_rejected.loc[df_rejected["id_missing"], "reason"] = "Missing ID"
df_rejected.loc[df_rejected["price_missing"], "reason"] = "Missing price"
df_rejected.loc[df_rejected["currency_missing"], "reason"] = "Missing currency"
df_rejected.loc[df_rejected["negative_price"], "reason"] = "Negative price"


# 7. ANALYTICS SUMMARY

analytics_summary = pd.DataFrame({
    "snittpris": [df_valid["price"].mean()],
    "medianpris": [df_valid["price"].median()],
    "antal_produkter": [len(df_valid)],
    "antal_produkter_med_saknat_pris": [df["price_missing"].sum()]
})

analytics_summary.to_csv("outputs/analytics_summary.csv", index=False)


# 8. PRICE ANALYSIS (BONUS)

# Top 10 most expensive
top_10_expensive = df_valid.sort_values(
    by="price",
    ascending=False
).head(10)

# Most deviating from mean
mean_price = df_valid["price"].mean()

df_valid["price_deviation"] = abs(df_valid["price"] - mean_price)

top_10_deviation = df_valid.sort_values(
    by="price_deviation",
    ascending=False
).head(10)

price_analysis = pd.concat([top_10_expensive, top_10_deviation])

price_analysis.to_csv("outputs/price_analysis.csv", index=False)



# 9. PRODUCT INSIGHTS

most_expensive = df_valid.sort_values(
    by="price",
    ascending=False
).head(1)

cheapest = df_valid.sort_values(
    by="price",
    ascending=True
).head(1)

print("\nMost expensive product:")
print(most_expensive)

print("\nCheapest product:")
print(cheapest)


# 10. SAVE REJECTED

df_rejected.to_csv("outputs/rejected_products.csv", index=False)


print("\nValid rows:")
print(df_valid)

print("\nRejected rows:")
print(df_rejected)

