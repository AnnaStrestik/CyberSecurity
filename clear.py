import pandas as pd

# vymena carek za mezeru u description
cyber = pd.read_csv("CA_dirty.csv", encoding="utf8")
cyber["Description"] = cyber["Description"].str.replace(",", " ")
cyber["Target"] = cyber["Target"].str.replace(",", " ")
cyber["Author"] = cyber["Author"].str.replace(",", " ")
cyber["Target_Class"] = cyber["Target_Class"].str.replace(",", " ")
cyber["Attack"] = cyber["Attack"].str.replace(",", " ")
cyber.to_csv("CA_bezcarek.csv")

# cyber = pd.read_csv("description.csv", encoding="utf8")
# cyber["Target"] = cyber["Target"].str.replace(",", "-carka-")
# cyber.to_csv("description.csv")