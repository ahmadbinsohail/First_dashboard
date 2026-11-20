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


pivot = (df[df["System Full"].isin(top_5_systems)].pivot_table(
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
lib = df.dropna(subset="Release Year").copy()
lib["Release Year"] = pd.to_datetime(lib["Release Year"]).dt.year 
#lib["Release Year"] = lib["Release Year"].astype(int)
counts = lib.groupby(["System Full","Release Year"]).size().unstack(fill_value=0)
#st.table(counts)

brand_release_peryear = lib.pivot_table(index="Release Year",columns="Brand",values="Game Name", aggfunc="count",fill_value=0)
#st.write(brand_release_peryear)

