from functions import get_players
import pandas as pd
import json

p = get_players("NFL")

plist = list(p.values())
player_df = [pd.DataFrame.from_dict(x) for x in plist]

print(player_df[1])