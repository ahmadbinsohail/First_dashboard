from pathlib import Path as P
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

pivot.plot(figsize=(10,5))
