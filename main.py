from pathlib import Path as P
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib as mpl
import seaborn as sb

try :
    dir = P(__file__).resolve().parent
except NameError :
    dir = P.cwd()
file_path = dir / "data"
df = pd.read_csv( file_path / "clean_games.csv",parse_dates=["Release Year"])
top_5_systems = df["System Full"].value_counts().head(5).index


pivot_5_systems = (df[df["System Full"].isin(top_5_systems)].pivot_table(
    index= "Release Year",
     columns="System Full",
      values="Units(m)" ,
      aggfunc="sum"))


#pivot.plot(figsize=(10,5))
#mpl.pyplot.show()
#st.line_chart(pivot)

conditions = [
    df["System Full"].str.contains("PlayStation|PSP|PS|VISIT|SONY",case=False,na=False),
    df["System Full"].str.contains("xbox|xbox360|xone",case=False,na=False),
    df["System Full"].str.contains("Nintendo|Wii|switch",case=False,na=False),
    df["System Full"].str.contains("Sega|Genesis|Dreamcast|Saturn",case=False,na=False)
]
brands = [ "Sony","Microsoft","Nintendo","Sega"]
df["Brand"] = np.select(conditions,brands,default="Other")
#st.write(df)
modified_df = df.dropna(subset="Release Year").copy()
modified_df["Release Year"] = pd.to_datetime(modified_df["Release Year"]).dt.year 
#lib["Release Year"] = lib["Release Year"].astype(int)
counts = modified_df.groupby(["System Full","Release Year"]).size().unstack(fill_value=0)
#st.table(counts)

games_peryear = modified_df.pivot_table(index="Release Year",columns="Brand",values="Game Name", aggfunc="count",fill_value=0)
#st.write(brand_release_peryear)

top_5_gamelibaray = df.groupby(["Release Year","Brand"])["Game Name"].size().unstack(fill_value=0)
st.line_chart(top_5_gamelibaray)

golden_era = modified_df.groupby("Release Year")[["Game Name"]].count()
st.write(golden_era.nlargest(1,"Game Name"))

brands_groupby_years = modified_df.groupby("Brand")["Release Year"].agg(First_Year="min",Last_Year="max",Totall_Games="size")
brands_groupby_years["Life_Span"] = brands_groupby_years["Last_Year"] - brands_groupby_years["First_Year"] + 1
st.write(brands_groupby_years)



dummy = modified_df.groupby(["Brand","Release Year"],as_index=False)["Game Name"].count().rename(columns={"Game Name":"Game Count"})

peak_year_by_brand = dummy.loc[dummy.groupby("Brand")["Game Count"].idxmax()].set_index("Brand")
st.write(peak_year_by_brand)



year = 1999
specific_year_games = dummy[dummy["Release Year"]==year]
st.write(specific_year_games)