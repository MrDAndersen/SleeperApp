from sleeper import SleeperBase

def get_players(sport):
  s = SleeperBase(sport)
  return(s.players())