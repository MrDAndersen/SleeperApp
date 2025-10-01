from sleeper import SleeperBase

class SleeperUserError(Exception):
    pass

class SleeperUser(SleeperBase):
    """
    Represents a user in the Sleeper API.

    Atributes:
        username (str): The user's username.
        user_id (str): The user's unique identifier.
        display_name (str): The user's display name.
        avatar (str): URL to the user's avatar image.
        current_season (str): The current season for the sport.
        endpoint (str): Base endpoint for user-related API requests.

    Methods:
        set_user(username: str = None, user_id: str = None) -> None:
            Sets the user's username or user_id.   
        get_user_leagues(season: str = None) -> dict:
            Retrieves the user's leagues for a specific season. If season is None, uses the current season.
        get_user_drafts(season: str = None) -> dict:
            Retrieves the user's drafts for a specific season. If season is None, uses the current season.
        user_info() -> dict:
            Returns a dictionary containing the user's information.
    """
    def __init__(self, username: str = None, user_id: str = None, sport: str = "NFL"):
        if not username and not user_id:
          raise SleeperUserError("🛡️ Please specify either username or user_id.")

        super().__init__(sport)
        self.endpoint = f"{self.BASE_URL}/user"
        self.current_season = self.state['data']['season']
        user_url = f"{self.endpoint}/{username if username else user_id}"
        user_info = self.send_request(user_url, None)
        self.username = user_info['data']['username']
        self.user_id = user_info['data']['user_id']
        self.display_name = user_info['data']['display_name']
        self.avatar = user_info['data']['avatar']

    def set_user(self, username: str = None, user_id: str = None) -> None:
        if (username):
            self.username = username
        if (user_id):
          self.user_id = user_id

    def get_user_leagues(self, season: str = None) -> dict:
        if not season:
          season = self.current_season

        u = f"{self.endpoint}/{self.user_id}/leagues/{self.sport}/{season}"
        return (self.send_request(u, None))

    def get_user_drafts(self, season: str = None) -> dict:
        if not season:
            season = self.current_season
        u = f"{self.endpoint}/{self.user_id}/drafts/{self.sport}/{season}"
        return (self.send_request(u, None))

    def user_info(self) -> dict:
        return {
            "username": self.username,
            "user_id": self.user_id,
            "display_name": self.display_name,
            "avatar": self.avatar,
            "season": self.current_season,
            "sport": self.sport
        }
