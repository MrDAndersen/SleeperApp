import requests
from urllib.parse import urljoin

class SleeperBase:
    """
    Base class for Sleeper API rituals.
    Codifies shared endpoints and contributor-safe request logic.
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
            print(f"[RuneError] Failed GET {url}: {e}")
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
        print(url)
        response = self._get(url, params)
        return {
            "headers": dict(response.get("headers", {})),
            "data": response.get("data", {})
        }
