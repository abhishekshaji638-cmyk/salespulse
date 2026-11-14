def validate(df):
    df = df.copy()
    df["Reason"] = ""   # empty means the row looks fine so far

    # helper: for every row where "mask" is True, add a reason text
    def flag(mask, text):
        df.loc[mask, "Reason"] = df.loc[mask, "Reason"] + text + "; "

    flag(df["OrderID"].isna(), "Missing Order ID")
    flag(df["ProductName"].isna(), "Missing product name")
    flag(df["Region"].isna(), "Missing region")
    flag(df["Quantity"] <= 0, "Quantity zero or negative")
    flag(df["UnitPrice"] <= 0, "Unit price zero or negative")
    flag(df["UnitCost"] < 0, "Negative unit cost")
    flag(df["OrderID"].notna() & df["OrderID"].duplicated(), "Duplicate Order ID")

    invalid = df[df["Reason"] != ""]
    valid = df[df["Reason"] == ""].drop(columns="Reason").copy()
    return valid, invalid