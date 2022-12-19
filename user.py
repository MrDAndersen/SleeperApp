from sleeper import SleeperBase


class SleeperUser(SleeperBase):

  def __init__(self, username=None, user_id=None, sport="NFL"):

    if not username and not user_id:
      raise Exception("Please specify either username or user_id.")

    super().__init__(sport)
    self.current_season = self.state['season']
    self.base_url = super().update_path("user/")
    user_url = self.update_path(f"{username if username else user_id}")
    user_info = self.send_request(user_url, None)
    self.username = user_info["username"]
    self.user_id = user_info["user_id"]
    self.display_name = user_info["display_name"]
    self.avatar = user_info["avatar"]

  def set_user(self, username=None, user_id=None):
    if (username):
      self.username = username
    if (user_id):
      self.user_id = user_id

  def get_user_leagues(self, season=None):
    if not season:
      season = self.current_season

    u = self.update_path(f"{self.user_id}/leagues/{self.sport}/{season}")
    return (self.send_request(u, None))

  def get_user_drafts(self, season=None):
    if not season:
      season = self.current_season
    u = self.update_path(f"{self.user_id}/drafts/{self.sport}/{season}")
    return (self.send_request(u, None))
