from urllib.parse import urlparse
import requests


class SleeperBase:
  base_url = None
  sport = None
  state = {}

  def __init__(self, sport):
    self.base_url = urlparse("https://api.sleeper.app/v1/")
    self.sport = str(sport).lower()
    self.state = self.send_request(self.update_path("state/" + self.sport),
                                   None)

  def update_path(self, p):
    return (self.base_url._replace(path=self.base_url.path + p.lower()))

  def send_request(self, url, params):
    res = requests.get(url.geturl(), params=params)
    return (res.json())

  def players(self):
    player_path = self.update_path(f"players/{self.sport}")
    return(self.send_request(player_path, None))

  def trending(self, type, lookback_hours = 24, limit=25):
    player_path = self.update_path(f"players/{self.sport}/trending/{type}")
    trending_params = {"lookback_hours": lookback_hours, "limit" : limit}
    return(self.send_request(player_path, trending_params))
