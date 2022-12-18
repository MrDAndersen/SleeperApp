from functions import get_players
import pandas as pd
import json

p = get_players("NFL")
l = [pd.DataFrame.from_dict(x, orient="index").transpose() for x in p.values()]
print(pd.concat(l))