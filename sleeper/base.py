import requests
from urllib.parse import urljoin

class SleeperBase:
    """
    Base class for Sleeper API rituals.
    Codifies shared endpoints and contributor-safe request logic.

    Attributes:
        BASE_URL (str): The base URL for the Sleeper API.
        sport (str): The sport for the API requests (e.g., "nfl", "nba").
        state (dict): The current state of the sport from the API.  
    
    Methods:
        _get(endpoint: str, params: dict = None) -> dict:
            Performs a GET request to the specified endpoint with optional parameters.
        get_players() -> dict:
            Retrieves the full player registry for the sport.
        get_trending_players(type: str, lookback_hours: int = 24, limit: int = 25) -> dict:
            Retrieves trending players by type (e.g., 'add', 'drop').
        update_path(path: str) -> str:
            Updates the base URL path for the API request.
        send_request(url: str, params: dict = None) -> dict:
            Sends a request to the specified URL with optional parameters and returns the response. 
    """
    BASE_URL = "https://api.sleeper.app/v1/"
    
    def __init__(self, sport: str):
        self.sport = sport.lower()
        self.state = self._get(f"state/{self.sport}")

    def _get(self, endpoint: str, params: dict = None):
        """
        Contributor-safe GET request with headers and symbolic error overlays.
        Returns a dictionary with 'data' and 'headers'.
        """
        url = urljoin(self.BASE_URL, endpoint)
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return {
                "data": response.json(),
                "headers": dict(response.headers)
            }
        except requests.RequestException as e:
            print(f"[Request Error] Failed GET {url}: {e}")
            return {
                "data": None,
                "headers": {}
            }


    def get_players(self):
        """
        Summons full player registry for the sport.
        """
        return self._get(f"players/{self.sport}")

    def get_trending_players(self, type: str, lookback_hours: int = 24, limit: int = 25):
        """
        Retrieves trending players by type (e.g. 'add', 'drop').
        """
        params = {"lookback_hours": lookback_hours, "limit": limit}
        return self._get(f"players/{self.sport}/trending/{type}", params)
    
    def update_path(self, path: str) -> str:
        """
        Updates the base URL path for the API request.
        """
        return urljoin(self.BASE_URL, path)

    def send_request(self, url: str, params: dict = None) -> dict:
        response = self._get(url, params)
        return {
            "headers": dict(response.get("headers", {})),
            "data": response.get("data", {})
        }
