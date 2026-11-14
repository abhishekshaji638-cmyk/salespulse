import pandas as pd
from validation import validate

df = pd.read_csv("data/sales.csv")
valid, invalid = validate(df)

print("Valid:", len(valid))
print("Invalid:", len(invalid))
print(invalid[["OrderID", "ProductName", "Region", "Reason"]])