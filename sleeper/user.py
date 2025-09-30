from sleeper import SleeperBase

class SleeperUserError(Exception):
    pass

class SleeperUser(SleeperBase):
    def __init__(self, username: str = None, user_id: str = None, sport: str = "NFL"):
        if not username and not user_id:
          raise SleeperUserError("🛡️ Please specify either username or user_id.")

        super().__init__(sport)
        self.current_season = self.state['data']['season']
        user_url = self.update_path(f"user/{username if username else user_id}")
        user_info = self.send_request(user_url, None)
        self.username = user_info['data']['username']
        self.user_id = user_info['data']['user_id']
        self.display_name = user_info['data']['display_name']
        self.avatar = user_info['data']['avatar']

    def set_user(self, username: str = None, user_id: str = None):
        if (username):
            self.username = username
        if (user_id):
          self.user_id = user_id

    def get_user_leagues(self, season: str = None):
        if not season:
          season = self.current_season

        u = self.update_path(f"/user/{self.user_id}/leagues/{self.sport}/{season}")
        return (self.send_request(u, None))

    def get_user_drafts(self, season: str = None):
        if not season:
            season = self.current_season
        u = self.update_path(f"/user/{self.user_id}/drafts/{self.sport}/{season}")
        return (self.send_request(u, None))

    def user_info(self):
        return {
            "username": self.username,
            "user_id": self.user_id,
            "display_name": self.display_name,
            "avatar": self.avatar,
            "season": self.current_season,
            "sport": self.sport
        }
