import pandas as pd
import numpy as np


df = pd.read_csv("data/products.csv", sep=";")

print(df.info())
print(df.head())

